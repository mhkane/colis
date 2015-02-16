from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from schemes import User, currentUser
from airspress.settings import CONFIG
from signup.schemes import save_user_pic, is_logged_in, re_validation, sign_in
from signup.forms import loginForm, registerForm

authomatic = Authomatic(CONFIG, 'a super secret random string about falconpress and his brethren')

def home(request):
    # Create links and sign-up form to forward to the Login handler.
    registerView = registerForm()
    loginView = loginForm()
    # Recover data from sessions
    cUser=None
    pPicture=''
    try:
        saken = request.session['lsten']
        cUser = currentUser(saken)
    except KeyError:
        return render(request, 'signup/index.html', 
                    {'loginView':loginView,'registerView':registerView,})
    
    if cUser is not None:
        objID = cUser['objectId']
        username = cUser['username']
        if objID:
            cUser = User.Query.get(objectId=objID)
            try:
                pPicture = cUser.profilePicture.url
            except AttributeError:
                pass
            return render(request, 'signup/index.html', 
                    {'loginView':loginView,'registerView':registerView,
                    'greetings':username, 'pPicture':pPicture})
    return render(request, 'signup/index.html', 
                    {'loginView':loginView,'registerView':registerView,})

def signup(request, provider_name):
    if provider_name == 'student':
        alert={'type':'','text':''} # dict type object to carry warnings or notifications to the front
        loginView=loginForm()
        cUser = is_logged_in(request)
        if not cUser:
            if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
                registerView = registerForm(request.POST)
                if registerView.is_valid():
                    #Sometimes there's no obvious errors but there are still errors...
                    alert = re_validation(registerView)
                    
                    print alert
                    if alert['type']=='success':
                        # clear form only if success because...
                        registerView=registerForm()
                    # ...Not every one love filling forms a dozen time, unless you're a robot ;)
                    if request.is_ajax():
                        return render(request,'signup/signup_ajx.html',{'loginView':loginView,'registerView':registerView,
                                                         'alert':alert})
                    else:
                        return HttpResponseRedirect(reverse('signup:register_success'))
     
            #Throwing back form on page with errors, alerts
                else:
                    print registerView.errors
                    if request.is_ajax():
                        return render(request,'signup/signup_ajx.html',
                            {'loginView':loginView,'registerView':registerView,
                            'alert':alert})
                    else:
                        return render(request,'signup/signup.html',
                            {'loginView':loginView,'registerView':registerView,
                            'alert':alert})
                
        else:
            return HttpResponseRedirect(reverse('trips:index'))
        registerView=registerForm()
        return render(request,'signup/signup.html',{'registerView':registerView,})
    return HttpResponseRedirect(reverse('signup:index'))#home page
            

def login(request, provider_name):
    '''
    Handles validating login form and sending validation emails
    Fire proper handler for each type of user i.e. student or student referrals
    '''
    registerView=registerForm()
    loginView=loginForm()
    if provider_name == 'student':
        alert={'type':'','text':''} # dict type object to carry warnings or notifications to the front
        cUser = is_logged_in(request)
        if not cUser:
            if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
                loginView = loginForm(request.POST)
                if loginView.is_valid():
                    #Sometimes there's no obvious errors but there are still errors...
                    alert = sign_in(request, loginView)
                    
                    print alert
                    #if login succeeded alert is in fact cUser object i.e. logged-in user 
                    if not isinstance(alert, dict):
                        # clear form only if success because...
                        loginView=loginForm()
                        # ...Not every one love filling forms a dozen time, unless you're a robot ;)
                        return HttpResponseRedirect(reverse('trips:index'))
                    else:
                        return render(request,'signup/signin_ajx.html',
                            {'loginView':loginView,'registerView':registerView,
                            'alert':alert})
     
            #Throwing back form on page with errors, alerts
                else:
                    print loginView.errors
                    alert={'type':'danger', 'text':'Some errors apparently...'}
                    if request.is_ajax():
                        return render(request,'signup/signin_ajx.html',
                            {'loginView':loginView,'registerView':registerView,
                            'alert':alert})
                    else:
                        return render(request,'signup/signin.html',
                            {'loginView':loginView,'alert':alert})
        # Or a user is connected and we see him to the trips page :)        
        else:
            return HttpResponseRedirect(reverse('trips:index'))
        # GET request. This is definitely someone who came all the way to login, no modals but the page
        return render(request,'signup/signin.html',{'loginView':loginView,})
    # return HttpResponseRedirect(reverse('signup:index'))#home page
    else:
        # We need the response object for the adapter.
        response = HttpResponse()
        
        # Start the login procedure.
        result = authomatic.login(DjangoAdapter(request, response), provider_name)
         
        # If there is no result, the login procedure is still pending.
        # Don't write anything to the response if there is no result!
        if result:
            # If there is result, the login procedure is over and we can write to response.
            #response.write('<a href="..">Home</a>')
            
            if result.error:
                # Login procedure finished with an error.
                response.write('<h2>Damn that error: {0}</h2>'.format(result.error.message))
            elif result.user:
                
                # OAuth 2.0 and OAuth 1.0a provide only limited user data on login,
                # We need to update the user to get more info.
                if not (result.user.name and result.user.id):
                    result.user.update()
                
                # Recover information for Parse authData
                #response.write(u'{0}'.format(result.user.name))
                fbID = result.user.id
                # response.write(u'<h2>Your email is: {0}</h2>'.format(result.user.email))
                
                # Seems like we're done, but there's more we can do...
                if result.user.credentials:
                    if result.provider.name == 'fb':
                        #serialized_credentials = result.user.credentials.serialize()
                        credentials = authomatic.credentials(result.user.credentials)
                        valid = credentials.valid
                        expiration_date = credentials.expiration_date
                        access_token = credentials.token
                        if valid:
                            authData = {"facebook": {"id": fbID, "access_token": access_token,
                             "expiration_date": expiration_date}}
                            account = User.login_auth(authData)
                            profilePicture = 'https://graph.facebook.com/'+fbID+'/picture?type=large'
                            explodeName = result.user.name.split(' ', 2) #Build username from FB name
                            PUsername = '_'.join(explodeName[:2 if len(explodeName)>2 else 1]) #join 2 first component of exploded name
                            account.username = PUsername if PUsername else result.user.name.replace(' ','')
                            account.save()
                            b = save_user_pic(account, fbId=fbID)
                            request.session['pPicture']= profilePicture
                            request.session['lsten'] = account.sessionToken
                            return HttpResponseRedirect(reverse('trips:index'))
                    else:
                        alert={'text':'Sign-in process has been aborted, try again please.'}
        
        return response          
                # If there are credentials (only by AuthorizationProvider),
                # we can _access user's protected res
def logout(request):
    try:
        request.session.flush()
    except:
        pass
    return HttpResponseRedirect(reverse('signup:index'))