from django.utils import timezone
import datetime
from trips.crtrips import trip
from trips.forms import searchForm
from parse_rest.user import User
import airspress
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
import urllib2
from parse_rest.datatypes import File
img = urllib2.urlopen("https://www.gravatar.com/avatar/c23cd2d6afb9dc3e42b6c0d280086fab?s=32&d=identicon&r=PG").read()
m = User.Query.get(username='m')
pic = m.profilePicture.url
print pic
