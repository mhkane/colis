from parse_rest.connection import register
from airspress import settings
import airspress
from airspress.settings import FILE_UPLOAD_DIR
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
    user_email = loginView.cleaned_data['login_email']
    user_password = loginView.cleaned_data['login_password']
    user_institution = loginView.cleaned_data['login_institution']
    accepted_institution=['Université Laval','Massachussets Institute of Technology','HEC Rabat', 'École Polytechnique de Montréal']
    domain_mail = {'Université Laval':'@ulaval.ca','Massachussets Institute of Technology':'@mit.edu'}
    alert={}
    email_existing='' # verifying existence of another user associated with this email address
    try:
        email_existing=User.Query.get(email=user_email).objectId
    except AttributeError:
        pass
    if email_existing:
        alert={'type':'danger', 'message':'This email is already in use...', 'message2':'Did you forget your password ?'}
        return alert
    if user_institution in accepted_institution:
        if domain_mail[user_institution] in user_email:
            new_user = User.signup(user_email, user_password, email=user_email)
            alert={'type':'success', 'message':'''Nearly done ! Please confirm
             your email address by following the link we sent you.'''}
        else:
            alert={'type':'warning','message':'You should use '+domain_mail[user_institution]+' email'}
    else:
        alert={'type':'warning','message':'We are not in your college yet but it won''t take long before we do'}
    return alert
def sign_in(username, user_password):
    cUser=User.login(username,user_password)
    try:
        user_id = cUser.objectId
    except AttributeError:
        pass
    if not user_id:
        alert={'type':'danger','message':'This user does not exist','message2':'Sign up here'}
        return alert
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
        urlpic = data['url']
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