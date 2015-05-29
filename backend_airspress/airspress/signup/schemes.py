from parse_rest.connection import register
from airspress import settings
from parse_rest.query import QueryResourceDoesNotExist
from parse_rest.core import ResourceRequestNotFound
from signup.backend_parse import passRequest, referral, Notifications
from string import split
#register to Parse
register(settings.APPLICATION_ID, settings.REST_API_KEY, master_key=settings.MASTER_KEY)#settings.REST_API_KEY
#from parse_rest.connection import ParseBatcher
#We override Django User class
from parse_rest.user import User as ParseUser

class User(ParseUser):
    pass
def currentUser(saken):
    '''
    This scheme just recover the current logged-in user on Parse.
    "saken" is the session token stored in a secure cookie on client side. 
    '''
    import json,httplib
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/users/me', '', {
       "X-Parse-Application-Id": settings.APPLICATION_ID,
       "X-Parse-REST-API-Key": settings.REST_API_KEY,
       "X-Parse-Session-Token": saken
     })
    result = json.loads(connection.getresponse().read())
    return result


def is_logged_in(request):# return the current user if User is still logged in.
    try:
        saken = request.session['lsten']
        cUser = currentUser(saken)
    except KeyError:
        return False
    if cUser:
        
        objID = cUser['objectId']
        if objID:
            cUserin = User.Query.get(objectId = objID) # unless we do that we can't operate it as a ParseUser
            cUserin.sessionToken = saken
            request.user_id = objID
            try:
                if not getattr(cUserin, 'notifications', False):
                    cUserin.notifications = Notifications.Query.get(targetUser = cUserin.objectId)
                    cUserin.save()
            except QueryResourceDoesNotExist:
                pass
            return cUserin
            
    
    return False

def re_validation(request, registerView, provider_name, referral_id=''):
    '''
    This is the signup scheme which handles the two types of signup
    and make the proper verifications
    '''
    from signup.backend_parse import Institutions
    user_name = registerView.cleaned_data['login_name']
    user_email = registerView.cleaned_data['login_email'].lower()
    user_password = registerView.cleaned_data['login_password']
    user_password_conf = registerView.cleaned_data['login_password_conf']
    try:
        user_institution = registerView.cleaned_data['login_institution']
    except KeyError:
        user_institution=''
    
    #This password validation line, shouldn't be kept but don't want 
    # to create subclass validation right now; TODO 
    # UPDATE: we created subclass validation, we should trash this one mwahahaha
    if not user_password == user_password_conf:
        alert={'type':'danger', 'text':'Hmmm... Passwords don''t match...'}
        return alert
    domain_mail = "@"
    if provider_name == 'student':
        # """Recover human readable names from the choiceField selectbox, yes it's that tedious hehe ;) """
        institution_dict = dict(registerView.fields['login_institution'].choices)
        accepted_institution = institution_dict[int(user_institution)]
        # Now we can get the domains associated with the selected institution
        try:
            domain_mail = Institutions.Query.get(name=accepted_institution).mailDomain
        except (AttributeError, QueryResourceDoesNotExist):
            alert={'type':'danger', 'text':'An error occured. Try again later...'}
            return alert
    # This alert dict will be returned with relevant notes 
    alert={} # alert["type"] and alert["text"] are mandatory, we can add other keywords
    email_existing='' 
    # verifying existence of another user associated with this email address
    try:
        email_existing=User.Query.get(email=user_email).objectId
    except (AttributeError, QueryResourceDoesNotExist):
        pass
    if email_existing:
        alert={'type':'danger', 'text':'This email is already in use...', 'link':'Did you forget your password ?'}
        return alert
    
    if domain_mail in user_email:
        if provider_name=='referral':
            try:
                this_referral = referral.Query.get(objectId=referral_id)
                new_user = User.signup(user_email, user_password, email=user_email, Name=user_name)
                new_user = User.login(user_email, user_password)
                new_user.referralInfo = this_referral
                new_user.save()
            except (QueryResourceDoesNotExist, ResourceRequestNotFound):
                alert={'type':'danger', 'text':'This referral link is not valid !'}
                return alert
           
        new_user = User.signup(user_email, user_password, email=user_email, Name=user_name)
        alert={'type':'success', 'text':'''Nearly done ! Please confirm
         your email address by following the link we sent you.'''}
        # We can login the user
        sign_in(request, login_dic={'username':user_email,'password':user_password})
        
    else:
        alert={'type':'warning','text':'You should use an "'+domain_mail+'" email address'}
    print alert    
    return alert

def sign_in(request, login_dic=None, loginView=None, provider_name='student'):
    '''
    This is the handler for login, "loginView" is the login form
    "loginView" is a form object containing login information
    "login_dic" is a dict object containing login information
    Both do not happen at the same time. 
    "login_dic" is mainly used outside the actual signing-in routine.
    Any of them will behave the same.
    '''
    #recover login information
    if loginView is not None:
        username = loginView.cleaned_data['login_username']
        user_pass = loginView.cleaned_data['login_password']
    elif login_dic is not None:
        username = login_dic['username']
        user_pass = login_dic['password']
    else:
        username = ''
        user_pass = username
    # try to login via PArse
    try:
        cUser=User.login(username,user_pass)
        user_id = cUser.objectId
    except (AttributeError, QueryResourceDoesNotExist,ResourceRequestNotFound):
        user_id=''
    #in case of error, check if username matches anything in the database
    if not user_id:
        try:
            is_user = User.Query.get(username=username)
        except (AttributeError, QueryResourceDoesNotExist):
            is_user=''
        if is_user:
            # match! so must have lost her keys 
            alert={'type':'warning','text':'Wrong Password !','link':'Forgot your password ?','url':'/password_reset/'}
        else:
            # hmm.. trying to plays us !?
            alert={'type':'danger','text':'This user does not exist','link':'Sign up here','url':'/register/student'}
        return alert
    #create a secure session server-side and a little cookie client side
    
    request.session['lsten']=cUser.sessionToken
    try:
        if not getattr(cUser, 'notifications', False):
            cUser.notifications = Notifications.Query.get(targetUser = cUser.objectId)
            cUser.save()
    except QueryResourceDoesNotExist:
        pass
    return cUser

def request_password(email):
    reference = ''
    try:
        this_user = User.Query.get(email=email)
        result = passRequest(userRequester=this_user)
        result.save()
        reference = result.objectId
    except (AttributeError, QueryResourceDoesNotExist):
        pass
    print reference
    return reference

def change_password(new_password, userid):
    import json,httplib
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('PUT', '/1/users/'+userid, json.dumps({
       "password": new_password
     }), 
    {"X-Parse-Application-Id": settings.APPLICATION_ID,
       "X-Parse-Master-Key": settings.MASTER_KEY,
       "Content-Type":"application/json" 
     })
    result = json.loads(connection.getresponse().read())
    print result
    return result

    

def verify_email(userid):
    import json,httplib
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('PUT', '/1/users/'+userid, json.dumps({
       "emailVerified": True
     }), 
    {"X-Parse-Application-Id": settings.APPLICATION_ID,
       "X-Parse-Master-Key": settings.MASTER_KEY,
       "Content-Type":"application/json" 
     })
    result = json.loads(connection.getresponse().read())
    print result
    return result 


def save_user_pic( account, fbId=None, filepath=None, filetype='image/jpeg', filext='jpg'):
    '''
    This is the picture uploader; it uploads a picture to Parse 
    and associate it with an User. Needs some revamping so we can upload pics
    in messages and requests as well.
    '''
    from airspress.settings import APPLICATION_ID, REST_API_KEY
    import urllib2
    import httplib
    import json
    print filetype
    print filext
    if fbId is not None:
        source = urllib2.urlopen('https://graph.facebook.com/v2.2/'+fbId+'/picture?redirect=0&type=large')
        filepath = settings.FILE_UPLOAD_DIR + fbId +'.jpg'
        user_id = account.objectId
        data = json.loads(source.read())
        print data
        urlpic = data['data']['url']
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('POST', '/1/files/pic1.'+str(filext), 
           urllib2.urlopen(urlpic).read(), 
            {
             "X-Parse-Application-Id": APPLICATION_ID,
               "X-Parse-REST-API-Key": REST_API_KEY, 
                "Content-Type": str(filetype)
             })
        picture = json.loads(connection.getresponse().read())
    else:
        user_id = account.objectId
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('POST', '/1/files/pic1.'+str(filext), 
        open(filepath,'rb').read(), 
        {
         "X-Parse-Application-Id": APPLICATION_ID,
           "X-Parse-REST-API-Key": REST_API_KEY, 
            "Content-Type": str(filetype)
         })
        picture = json.loads(connection.getresponse().read())
    print picture
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('PUT', '/1/users/'+user_id, json.dumps({                                             
           "profilePicture": {
             "name": picture['name'],
             "__type": "File"
           }
         }), {
           "X-Parse-Application-Id": APPLICATION_ID,
           "X-Parse-REST-API-Key": REST_API_KEY,
           "X-Parse-Session-Token": account.sessionToken,
           "Content-Type": "application/json"
         })
    result = json.loads(connection.getresponse().read())
    print result
    profilePic=''
    try:
        profilePic = account.profilePicture.url
    except AttributeError:
        pass
    return profilePic

import tempfile
import shutil

FILE_UPLOAD_DIR = settings.FILE_UPLOAD_DIR

def handle_uploaded_file(source, cUser):
    '''
    This is a helper for the uploader; creates a local tempfile to host user-uploaded file
    on server before it's sent to Parse.com
    '''
    if not source:
        return False
    import os
    fd, filepath = tempfile.mkstemp(prefix=source.name, dir=FILE_UPLOAD_DIR)
    with open(filepath, 'wb+') as dest:
        shutil.copyfileobj(source, dest)
    verify = save_user_pic(account=cUser, filepath=filepath, filetype=source.content_type, filext=split(source.name,sep='.')[-1])
    try:
        os.remove(filepath)
    except OSError:
        pass
    return verify

