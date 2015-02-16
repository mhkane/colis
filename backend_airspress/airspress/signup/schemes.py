from parse_rest.connection import register
from airspress import settings
import airspress
from airspress.settings import FILE_UPLOAD_DIR
from parse_rest.query import QueryResourceDoesNotExist
#register to Parse
register(settings.APPLICATION_ID, settings.REST_API_KEY)#settings.REST_API_KEY
from parse_rest.connection import ParseBatcher
# Object Alias to differentiate from python objects
from parse_rest.datatypes import Object as ParseObject
#We override Django User class
from parse_rest.user import User as ParseUser

class User(ParseUser):
    pass
def currentUser(saken):
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
def is_logged_in(request):# return the current user if User logged in.
    try:
        saken = request.session['lsten']
        cUser = currentUser(saken)
    except KeyError:
        return False
    if cUser is not None:
        objID = cUser['objectId']
        if objID:
            cUserin = User.Query.get(objectId = objID) # unless we do that we can't operate it as a ParseUser
            return cUserin
    
    return False
def re_validation(loginView):
    from signup.backend_parse import Institutions
    user_email = loginView.cleaned_data['login_email']
    user_password = loginView.cleaned_data['login_password']
    user_password_conf = loginView.cleaned_data['login_password_conf']
    user_institution = loginView.cleaned_data['login_institution']
    user_name = loginView.cleaned_data['login_name']
    #This shouldn't be kept but don't want to create subclass validation right now; TODO 
    if not user_password == user_password_conf:
        alert={'type':'danger', 'text':'Hmmm... Passwords don''t match...'}
        return alert
    # """Recover human readable names from the choiceField selectbox, yes it's that tedious hehe ;) """
    institution_dict = dict(loginView.fields['login_institution'].choices)
    accepted_institution = institution_dict[int(user_institution)]
    # Now we can get the domains associated with the selected institution
    try:
        domain_mail = Institutions.Query.get(name=accepted_institution).mailDomain
    except (AttributeError, QueryResourceDoesNotExist):
        domain_mail=''
    # This alert dict will be returned with relevant notes 
    alert={'type':'','text':''}
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
        new_user = User.signup(user_email, user_password, email=user_email, Name=user_name)
        alert={'type':'success', 'text':'''Nearly done ! Please confirm
         your email address by following the link we sent you.'''}
    else:
        alert={'type':'warning','text':'You should use an "'+domain_mail+'" email address'}
    return alert
def sign_in(request, loginView):
    username = loginView.cleaned_data['login_username']
    user_pass = loginView.cleaned_data['login_password']
    try:
        cUser=User.login(username,user_pass)
        user_id = cUser.objectId
    except (AttributeError, QueryResourceDoesNotExist):
        user_id=''
    if not user_id:
        try:
            is_user = User.Query.get(username=username)
        except (AttributeError, QueryResourceDoesNotExist):
            is_user=''
        if is_user:
            alert={'type':'warning','text':'Wrong Password !','link':'Forgot your password ?','url':'/password_reset/'}
        else:
            alert={'type':'danger','text':'This user does not exist','link':'Sign up here','url':'/login/student'}
        return alert
    request.session['lsten']=cUser.sessionToken
    return cUser
    
import airspress.settings
def save_user_pic( account, fbId=None, filepath=None):
    import urllib2
    import httplib
    import json
    if fbId is not None:
        source = urllib2.urlopen('https://graph.facebook.com/v2.2/'+fbId+'/picture?redirect=0&type=large')
        filepath = settings.FILE_UPLOAD_DIR + fbId +'.jpg'
        user_id = account.objectId
        data = json.loads(source.read())
        print data
        urlpic = data['data']['url']
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('POST', '/1/files/pic1.jpg', 
           urllib2.urlopen(urlpic).read(), 
            {
             "X-Parse-Application-Id": airspress.settings.APPLICATION_ID,
               "X-Parse-REST-API-Key": airspress.settings.REST_API_KEY, 
                "Content-Type": "image/jpeg"
             })
        picture = json.loads(connection.getresponse().read())
    else:
        user_id = account.objectId
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        connection.request('POST', '/1/files/pic1.jpg', 
        open(filepath,'rb').read(), 
        {
         "X-Parse-Application-Id": airspress.settings.APPLICATION_ID,
           "X-Parse-REST-API-Key": airspress.settings.REST_API_KEY, 
            "Content-Type": "image/jpeg"
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
           "X-Parse-Application-Id": airspress.settings.APPLICATION_ID,
           "X-Parse-REST-API-Key": airspress.settings.REST_API_KEY,
           "Content-Type": "application/json"
         })
    result = json.loads(connection.getresponse().read())
    print result
    profilePic=''
    try:
        profilePic = account.profilePicture.url
    except AttributeError:
        profilePic = ''
    return profilePic

import tempfile
import shutil

FILE_UPLOAD_DIR = settings.FILE_UPLOAD_DIR

def handle_uploaded_file(source, cUser):
    fd, filepath = tempfile.mkstemp(prefix=source.name, dir=FILE_UPLOAD_DIR)
    with open(filepath, 'wb+') as dest:
        shutil.copyfileobj(source, dest)
    verify = save_user_pic(account=cUser, filepath=filepath)
    return verify
