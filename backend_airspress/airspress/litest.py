from django.utils import timezone
import datetime
from trips.crtrips import trip
from trips.forms import searchForm
from parse_rest.user import User
import airspress
from parse_rest.installation import Push
from account.actions import notif_mail
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
k=notif_mail("konoufo@hotmail.fr","Mohamed","accepted your request")
