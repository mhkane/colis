
from parse_rest.connection import register
from airspress import settings
from django.utils import timezone
import datetime
register(settings.APPLICATION_ID, settings.REST_API_KEY)#settings.REST_API_KEY
from parse_rest.datatypes import Object as ParseObject
from parse_rest.user import User
class trip(ParseObject):
    pass
def tripFind(request, cUser, searchView):
    '''
    This is basically our search engine for finding trips in our database
    '''
    cityArr = searchView.cleaned_data['cityArr']
    cityDep = searchView.cleaned_data['cityDep']
    depDate1 = searchView.cleaned_data['depDate1']
    depDate2 = searchView.cleaned_data['depDate2']
    print depDate2, depDate1 #remove
    if depDate1 is None:
        depDate1 = timezone.now()
    else:
        depDate1 = datetime.datetime.combine(depDate1, datetime.time())
    if depDate2 is None:
        depDate2 = depDate1 + datetime.timedelta(days=90)
    else:
        depDate2 = datetime.datetime.combine(depDate2, datetime.time())
    allTrips = trip.Query.filter(objectId='')
    #Different queries depending if cities are left blank or not
    print depDate1, depDate2#remove
    if not cityDep and not cityArr :
            allTrips = trip.Query.filter(fromLocation__ne='', toLocation__ne = '', departureDate__gte = depDate1, 
                                    departureDate__lte = depDate2)
    elif not cityDep:
            allTrips = trip.Query.filter(toLocation__ne = '', departureDate__gte = depDate1, 
                                    fromLocation__in=[cityDep], departureDate__lte = depDate2)
    elif not cityArr:
            allTrips = trip.Query.filter(fromLocation__ne = '', departureDate__gte = depDate1, 
                                    toLocation__in=[cityArr], departureDate__lte = depDate2)
    else:
            allTrips = trip.Query.filter(fromLocation__ne='', toLocation__ne = '', 
                                         departureDate__gte = depDate1, departureDate__lte = depDate2)
    print allTrips#remove
    page_one = allTrips
    k = 0
    tripDict = {}
    for anyTrip in page_one :
        k = k + 1
        pub_date = ''
        travelerUser = ''
        departDate = ''
        destLocation = ''
        oriLocation = ''
        travelerId = False
        try:
            pub_date = anyTrip.createdAt
            travelerId  = anyTrip.traveler.objectId
            departDate = anyTrip.departureDate
            destLocation = anyTrip.toLocation
            oriLocation = anyTrip.fromLocation
        except AttributeError:
            pass
        
        if travelerId:#use travelerId to access traveler info
            travelerUser = User.Query.get(objectId=travelerId).username
            if travelerUser == '':
                pass
            else:
                tripDict['objTrip'+str(k)] = {'pub_date':pub_date, 
                'travelerUser':travelerUser, 'departDate':departDate, 
                'destLocation':destLocation, 'oriLocation':oriLocation,}
                #once the context dict created we can use render()
                print(tripDict)
                print k+1

    return tripDict