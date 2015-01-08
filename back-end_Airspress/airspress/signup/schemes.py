from parse_rest.connection import register
from airspress import settings
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