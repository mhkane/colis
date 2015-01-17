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
import airspress.settings
def getFbpic( account, fbId=None, filepath=None, saken=None):
    import urllib

    if fbId is not None:
        source = 'http://graph.facebook.com/'+fbId+'/picture?type=large'
        filepath = settings.FILE_UPLOAD_DIR + fbId +'.jpg'
        saken = account.sessionToken
        f = open(filepath,'w+b')
        f.write(urllib.urlopen(source).read())
        f.close()
    import json,httplib
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
    connection.request('POST', '/1/users/me', json.dumps({
            "username":account.username,                                              
           "profilePicture": {
             "name": picture['name'],
             "__type": "File"
           }
         }), {
           "X-Parse-Application-Id": airspress.settings.APPLICATION_ID,
           "X-Parse-REST-API-Key": airspress.settings.REST_API_KEY,
           "X-Parse-Session-Token": saken,
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

def handle_uploaded_file(source, saken):
    fd, filepath = tempfile.mkstemp(prefix=source.name, dir=FILE_UPLOAD_DIR)
    with open(filepath, 'wb') as dest:
        shutil.copyfileobj(source, dest)
    verify = getFbpic(saken=saken, filepath=filepath)
    return verify