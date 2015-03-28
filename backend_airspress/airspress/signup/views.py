from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from schemes import User, currentUser
from airspress.settings import CONFIG
from signup.schemes import save_user_pic, is_logged_in, re_validation, sign_in,\
    request_password, change_password, verify_email
from signup.forms import loginForm, registerForm, ref_regForm, change_passForm,\
    email_askForm
from account.actions import referral, send_mail
from parse_rest.query import QueryResourceDoesNotExist
from signup.backend_parse import passRequest
from django.contrib.sites.models import get_current_site

authomatic = Authomatic(CONFIG, 'a super secret random string about falconpress and his brethren')

def home(request):
    '''
    This is the home page view. When anyone try to access any link 
    on the domain i.e. "airspress.com/profile/" while not logged in
    he/she is redirected here. One thing we can improve is adding a
    "you have been disconnected"-like alert when a previously logged-in
    try to access a timed-out session.
    
    '''
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
        #This is basically the sole instance where cUser is a dict object and not a ParseObject
        # This part(next 7 lines) is absolutely unnecessary, we should just redirect to Trip view
        # Question is : So why the f**ck am i writing that ?
        objID = cUser['objectId']
        username = cUser['username']
        if objID:
            try:
                cUser = User.Query.get(objectId=objID)
                pPicture = cUser.profilePicture.url
            except (AttributeError, QueryResourceDoesNotExist):
                pass
            return HttpResponseRedirect(reverse('trips:index')) 
        #render(request, 'signup/index.html', 
        #           {'loginView':loginView,'registerView':registerView,
        #          'greetings':username, 'pPicture':pPicture})
    return render(request, 'signup/index.html', 
                    {'loginView':loginView,'registerView':registerView,})

def signup(request, provider_name):
    """
    This is really self-descripting. But well we might get Alzheimer some day... 
    So provider_name is an URL argument which tells us which kind of sign-up 
    is going on. Once we catch it we route the signup form to the proper handler.
    """
    if provider_name == 'student':
        alert={'type':'','text':''} # dict type object to carry warnings or notifications to the front
        loginView=loginForm()
        cUser = is_logged_in(request)
        if not cUser:
            if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
                registerView = registerForm(request.POST)
                if registerView.is_valid() and registerView.clean_login_password_conf():
                    #Sometimes there's no obvious errors but there are still errors...
                    alert = re_validation(registerView, provider_name)
                    
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
    elif provider_name == "referral":#referral
        if request.method == "POST":
            #referred user is already on the referral signup page
            #and he's signing up
            ref_regView = ref_regForm(request.POST)
            if ref_regView.is_valid():
                #Sometimes there's no obvious errors but there are still errors...
                alert = re_validation(ref_regView)
                
                print alert
                if alert['type']=='success':
                    # clear form only if success because...
                    ref_regView=registerForm()
                # ...Not every one love filling forms a dozen time, unless you're a robot ;)
                if request.is_ajax():
                    return render(request,'signup/signup_ajx.html',{'loginView':loginView,'ref_regView':ref_regView,
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
            #referred user is getting at the referral signup page
            ref_regView = ref_regForm()
            loginView = loginForm()
            referred_id = request.GET.get('referral','')#here we get the "?referral=" parameter
            if referred_id:
                try:
                    referral_obj = referral.Query.get(objectId=referred_id)
                    #if we're still here, existing referral is confirmed, we can signup the user
                    #signup routine should create referralInfo column to store a pointer to the referral object
                    #which contains the referrer, and other userful info. Other than that it's the same as previous
                    return render(request,'signup/signup.html',{'ref_regView':ref_regView,'loginView':loginView})
                except (AttributeError, QueryResourceDoesNotExist):
                    referral_obj=''
    return HttpResponseRedirect(reverse('signup:index'))#home page
            

def login(request, provider_name):
    '''
    Handles validating login form and sending validation emails
    Fire proper handler for each type of user i.e. student or student referrals
    '''
    registerView=registerForm()
    loginView=loginForm()

    alert={'type':'','text':''} # dict type object to carry warnings or notifications to the front
    cUser = is_logged_in(request)
    if not cUser:
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            loginView = loginForm(request.POST)
            if loginView.is_valid():
                #Sometimes there's no obvious errors but there are still errors... So we get to verify again before login   
                alert = sign_in(request, loginView, provider_name)
                
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
                 
def logout(request):
    try:
        request.session.flush()
    except:
        pass
    return HttpResponseRedirect(reverse('signup:index'))
def mail_confirmation(request):
    ''' There are some operations that need for security purposes, to
    ask for an email confirmation e.g. "password reset", "signup". 
    This view is the one which is called when getting a logged-off user email address
    is absolutely necessary i.e. it's not used for signup because 
    we have an email address field in the signup form '''
    alert={}
    if request.method == 'POST':
        email_address = email_askForm(request.POST)
        if email_address.is_valid():
            route = request.POST.get('next','')
            if route == 'reset_password':
                email = email_address.cleaned_data['email']
                pass_request_id = request_password(email) # pass_request_id is for constructing unique link that will be used
                if pass_request_id :
                    msg = 'You requested a Password reset on Airspress.com . Follow this link to change your password: \n'
                    link = ''.join(['http://', get_current_site(request).domain,reverse('signup:reset_pass')+'?jeton='+pass_request_id])
                    subject="Password Reset requested"
                    
                    try:
                        #send a mail with when necessary a link to the next step e.g. password reset
                        send_mail(text= msg + link + '\n',
                                  subject=subject, from_email="no-reply@airspress.com",
                                  from_name="Airspress", email=email, to_name='')
                        alert = {'type':'success','message':'Check your inbox, we sent out a link to reset your password'}
                    except (AttributeError, QueryResourceDoesNotExist):
                        alert = {'type':'warning','message':'There is a problem with the your request. Retry Later'}
                    
                else :
                    alert = {'type':'danger','message':'This email address isn''t associated with any user.'}
                    
                return render(request,'signup/ask_email.html',{'alert':alert, 'email':email_address})   
            else:
                return HttpResponseRedirect(reverse('signup:index'))
        else:
            print email_address.errors
        return render(request,'signup/ask_email.html',{'alert':alert, 'email':email_address})
    elif request.GET.get('token','') and request.GET.get('username',''):
        '''Signup email verification signal is caught here and email verified get set to True'''
        username = request.GET.get('username','')
        try:
            userid = User.Query.get(username=username).objectId
            result = verify_email(userid)
            alert={'type':'success', 
                   'text':'Your email address has been verified! Go on, add your trips and make your requests',
                   'link':'/login/student/'}
            return render(request,'signup/ask_email.html',{'alert':alert})

        except (AttributeError, QueryResourceDoesNotExist):
            pass
    # 'route' content identify the process which required an email confirmation
    # any frontend link to access this view should have a 'next' parameter which indicates the 
    #upcoming process e.g. www.airspress.com/mail_confimation?next=reset_password
    route = request.GET.get('next','')
    email_address = email_askForm()
    return render(request,'signup/ask_email.html',{'email':email_address,'route':route})
def pass_reset(request):
    ''' This view is as the name suggest is intended to display a form for the
    user to change the password. A unique password-changing link to access this view 
    is generated in mail_confirmation where it was sent out to the user.'''
    alert={}
    pass_request_id=''
    if request.method == 'POST':
        change_passView = change_passForm(request.POST)
        if change_passView.is_valid():
            #
            alert = {'type':'success','message':'Your Password was succesfully changed ! Login ','link':'here', 'url':'/login/student/en/'}#,'url':'/login/'}
            try:
                pass_request_id = request.POST.get('jeton','')
                cUser = passRequest.Query.get(objectId=pass_request_id).userRequester
                print cUser
                #cUser.save()
                new_password = change_passView.cleaned_data['new_pass_conf']
                result = change_password(new_password, cUser.objectId)
                print cUser
            except (AttributeError, QueryResourceDoesNotExist):
                alert = {'type':'warning','message':'There is a problem with the servers. Retry Later'}
        elif not change_passView.clean_new_pass_conf():
            alert = {'type':'warning','text':"Passwords don't match ."}

        
        else:
            print change_passView.errors
        return render(request,'signup/password_change.html',{'alert':alert, 'change_pass':change_passView, 'pass_request':pass_request_id })
    # this id will be placed in the upcoming POST information and will be used 
    # to identify which user new password request is being completed
    pass_request_id = request.GET.get('jeton','') 
    change_passView = change_passForm()
    return render(request,'signup/password_change.html',{'pass_request':pass_request_id, 'change_pass':change_passView})
def pre_pass_reset(request):
    """ This view has no frontend display, it just catches
    the request to reset password
    and then redirect to mail_confirmation view  """
    return HttpResponseRedirect(reverse('signup:mailconf')+'?next=reset_password')

# This was an attempt to simply use Parse.com 'ready-to-use' Password reset routine
# but will get 'parseapps.com' links (not very good for business ;) )
# or we could have paid to enable the use of a custom domain. Well i had a spare
#brain cell and decided it could be fun building our own routine.
# But i will just leave it here, it's not used for anything. 
    
def switch_pass(request):
    cUser = is_logged_in(request)
    alert={}
    if cUser:
        try:
            email = cUser.email
            cUser.request_password_reset(email=email) # we can't use that, we customize process
            alert['type']='success'
            alert['text']='Check your inbox, we sent out a link to reset your password'
            return render(request,'signup/password_change.html', {'alert':alert})
        except (AttributeError, QueryResourceDoesNotExist):
            alert={'type':'danger','text':'There seem to be a problem. Try again later.'}
            return render(request,'signup/password_change.html', {'alert':alert})
    return HttpResponseRedirect(reverse('signup:index'))
