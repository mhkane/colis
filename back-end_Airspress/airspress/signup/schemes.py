from parse_rest.connection import register
from airspress import settings
#register to Parse
register(settings.APPLICATION_ID, settings.REST_API_KEY)#settings.REST_API_KEY
from parse_rest.connection import ParseBatcher
# Object Alias to differentiate from python objects
from parse_rest.datatypes import Object as ParseObject
#We override Django User class
from parse_rest.user import User

class User(User):
    pass
class Trip(object):
    pass