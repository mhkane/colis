from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from schemes import User, currentUser
from airspress.settings import CONFIG
from signup.schemes import save_user_pic, is_logged_in, re_validation, sign_in
from signup.forms import loginForm, registerForm, ref_regForm, change_passForm,\
    email_askForm
from account.actions import referral, send_mail
from parse_rest.query import QueryResourceDoesNotExist

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
                if registerView.is_valid() and registerView.clean_password2():
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
    ask for a mail confirmation e.g. "password reset", "signup". 
    This view is the one which is called when getting only the user email address
    is absolutely necessary i.e. it's not for signup because 
    we have the email address from signup form '''
    alert={}
    if request.method == 'POST':
        email_address = email_askForm(request.POST)
        if email_address.isvalid():
            # route = POst['route']
            # reference = change_pass # reference is for constructing unique link that will be used
            #if reference :
            try:
                #send a mail with when necessary a link to the next step e.g. password reset
                send_mail(text='')
            except (AttributeError, QueryResourceDoesNotExist):
                alert = {'type':'warning','message':'There is a problem with the servers. Retry Later'}
            alert = {'type':'success','message':'Your Password was succesfully changed !'}
        
        else:
            print email_address.errors
        return render(request,'signup/ask_email.html',{'alert':alert, 'email':email_address})
    # route = request.GET.get('next','')
    email_address = email_askForm()
    return render(request,'signup/ask_email.html',{'email':email_address})
def new_password(request):
    ''' This view is as the name suggest intended to display a form for the
    user to change the password. The unique password changing link is generated from
    mail_confirmation.'''
    alert={}
    if request.method == 'POST':
        change_passView = change_passForm(request.POST)
        if change_passView.isvalid() and change_passView.clean_password2():
            #
            alert = {'type':'success','message':'Your Password was succesfully changed !'}
            try:
                pass_request_id = request.POST['pass_request']
                cUser = passRequest.Query.get(objectId=pass_request_id).userRequester
                cUser.request_password_reset(email=cUser.email)
                cUser.password = change_passView.clean_password2()
                cUser.save()
            except (AttributeError, QueryResourceDoesNotExist):
                alert = {'type':'warning','message':'There is a problem with the servers. Retry Later'}

        
        else:
            print change_passView.errors
        return render(request,'signup/password_change.html',{'alert':alert, 'change_pass':change_passView })
    pass_request_id = request.get.GET('jeton')
    return render(request,'signup/password_change.html',{'pass_request':pass_request_id})
def switch_pass(request):
    cUser = is_logged_in(request)
    alert={}
    if cUser:
        try:
            email = cUser.email
            cUser.request_password_reset(email=email)
            alert['type']='success'
            alert['text']='Check your inbox, we sent out a link to reset your password'
            return render(request,'signup/password_change.html', {'alert':alert})
        except (AttributeError, QueryResourceDoesNotExist):
            alert={'type':'danger','text':'There seem to be a problem. Try again later.'}
            return render(request,'signup/password_change.html', {'alert':alert})
    return HttpResponseRedirect(reverse('signup:index'))
            return render(request,'signup/password_change.html', {'alert':alert})