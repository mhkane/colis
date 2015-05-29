from django.utils import timezone
import datetime
from trips.crtrips import trip
from trips.forms import searchForm
from parse_rest.user import User
import airspress
from parse_rest.installation import Push
from signup.schemes import change_password
from parse_rest.connection import ParseBatcher
from texto_airspress.schemes import retrieve_conversation
from airspress import settings
cityDep = 'The bottom'
cityArr = 'The top'
depDate1=timezone.now()
adata = timezone.now() + datetime.timedelta(days=5)
depDate2=adata
# tripy = trip(toLocation = 'Paris, France', fromLocation = 'London, Canada', departureDate=adata)
# tripy.save()
# tripy = trip(toLocation = 'Lyon, France', fromLocation = 'London, Canada', departureDate=adata)
# tripy.save()
# adata+=datetime.timedelta(days=2)
# tripy = trip(toLocation = 'Bordeaux, France', fromLocation = 'Toronto, Canada', departureDate=adata)
# tripy.save()
# adata+=datetime.timedelta(days=3)
# tripy = trip(toLocation = 'Nice, France', fromLocation = 'London, England', departureDate=adata)
# tripy.save()
# adata+=datetime.timedelta(days=10)
# tripy = trip(toLocation = 'Nice, France', fromLocation = 'Paris, France', departureDate=adata)
# tripy.traveler = User.Query.get(objectId='A2NTGJxHJr')
# tripy.save()
# print(searchForm())
# data = {'depDate1':'2015-01-07'}
# boo = searchForm(data)
# if boo.is_valid():
#     pass
# print boo.errors
# tripy= trip.Query.filter(fromLocation__ne='', toLocation__ne = '', departureDate__gte = depDate1, departureDate__lte = depDate2)
# print tripy
# import urllib2
# import json
# from parse_rest.datatypes import File
# img = urllib2.urlopen("https://graph.facebook.com/40796308305/?fields=picture.type(large)")
# print img
# dict = json.loads(img.read())
# print dict
# urlpic = dict['picture']['data']['url']
# picture = urllib2.urlopen(urlpic)
# f = open("c:/cocacola.jpg","wb+")
# f.write(picture.read()) # save the pic
# f.close()
# # m = User.Query.get(username='m')
# # pic = m.profilePicture.url
# # print pic
# push_alert = 'Mohamed_K. accepted your request!'
# Push.alert({"alert": push_alert,
#                                  "badge": "Increment"}, where={"appUser":{"__type":"Pointer","className":"_User","objectId":"LKfygJctc7"}})
# k=change_password('marsiale','9lTLf3GPg1')
# print k
# from trips.crtrips import priceCalc
# 
# print priceCalc(5,25)

# import re
#  
# tokenize = lambda x: [i for i in re.findall(r'\w+', unicode(x).lower(), flags= re.UNICODE) if i]
#  
# list=[]
# alltrips = trip.Query.all()
# for atrip in alltrips:
#     citydep = unicode(atrip.fromLocation)
#     cityarr = unicode(atrip.toLocation)
#     atrip.toLocationTokens = tokenize(cityarr)
#     atrip.fromLocationTokens = tokenize(citydep)
#     list.append(atrip)
#     print atrip.fromLocationTokens, atrip.toLocationTokens
#        
# s = ParseBatcher().batch_save(list)
# print s

# convos = retrieve_conversation('9lTLf3GPg1')  
# print convos
#

import json
import httplib
filepath = 'C:\logo-bright.png'
filext = 'png'
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/logo-airspress.'+str(filext), 
open(str(filepath),'rb').read(), 
{
 "X-Parse-Application-Id": settings.APPLICATION_ID,
   "X-Parse-REST-API-Key": settings.REST_API_KEY, 
    "Content-Type": 'image/png'
 })
picture = json.loads(connection.getresponse().read())
print picture
with open('c:\logo_url.txt','w') as f :
    f.write(picture['url'])



