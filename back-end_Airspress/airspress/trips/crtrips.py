
from parse_rest.connection import register
from airspress import settings
register(settings.APPLICATION_ID, settings.REST_API_KEY)#settings.REST_API_KEY
from parse_rest.datatypes import Object as ParseObject

class trip(ParseObject):
    pass