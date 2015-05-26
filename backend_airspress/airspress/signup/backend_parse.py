from parse_rest.connection import register
from airspress import settings
#register to Parse
register(settings.APPLICATION_ID, settings.REST_API_KEY)#settings.REST_API_KEY
from parse_rest.connection import ParseBatcher
# Object Alias to differentiate from python objects
from parse_rest.datatypes import Object as ParseObject

class Institutions(ParseObject):
    pass
class passRequest(ParseObject):
    pass
class review(ParseObject):
    pass
class Item(ParseObject):
    pass
# request class is renamed as trequests so that to avoid
# redondance of the name with the request objet of views
class request(ParseObject):
    pass
class trequests(request):
    pass
# we have a referral class which is useful for retaining information between the referred and the referrer
# And there is the secret-word the referred enter at signup, best way to store that
class referral(ParseObject):
    pass