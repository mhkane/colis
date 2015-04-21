
from parse_rest.connection import register
from airspress import settings
from django.utils import timezone
import datetime
from time import strptime
from moneyed.classes import Money
from string import split
from signup.backend_parse import Item
register(settings.APPLICATION_ID, settings.REST_API_KEY)#settings.REST_API_KEY
from parse_rest.datatypes import Object as ParseObject
from parse_rest.user import User
from account.actions import request as trequests

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
        tripId = ''
        pPicture=''
        try:
            pub_date = anyTrip.createdAt
            travelerId  = anyTrip.traveler.objectId
            departDate = anyTrip.departureDate.date()
            destLocation = anyTrip.toLocation
            oriLocation = anyTrip.fromLocation
            tripId = anyTrip.objectId
            pPicture = User.Query.get(objectId=travelerId).profilePicture.url
        except AttributeError:
            pass
        
        if travelerId:#use travelerId to access traveler info
            travelerUser = User.Query.get(objectId=travelerId).username
            if travelerUser == '':
                pass
            else:
                areas_ori_location = split(oriLocation,',') 
                areas_dest_location = split(destLocation,',')
                destCountry = areas_dest_location[-1]
                destCity = areas_dest_location[1]
                oriCountry = areas_ori_location[-1]
                oriCity = areas_ori_location[1]
                tripDict['objTrip'+str(k)] = {'pub_date':pub_date, 
                'travelerUser':travelerUser, 
                'departDate':{'month':departDate.strftime("%B"), 'day':departDate.day},
                'destLocation':{'city':destCity,'country':destCountry}, 
                'oriLocation':{'city':oriCity,'country':oriCountry}, 'tripId':tripId, 'pPicture':pPicture,}
                #once the context dict created we can use render()
                print(tripDict)
                print k+1

    return tripDict
def tripCreate(request, cUser, addView):
    cityArr = addView.cleaned_data['cityArr']
    cityDep = addView.cleaned_data['cityDep']
    depDate = addView.cleaned_data['depDate']
    arrivDate = addView.cleaned_data['arrivDate']
    weightGood = addView.cleaned_data['weightGood']
    distance = 1000 #must be evaluated with another form field
    unitPrice = priceCalc(weightGood, distance)
    depDate = datetime.datetime.combine(depDate, datetime.time.min)
    arrivDate = datetime.datetime.combine(arrivDate, datetime.time.min)
    print depDate
    print arrivDate#remove
    newTrip = trip(departureDate = depDate, arrivalDate = arrivDate, fromLocation = cityDep, 
                toLocation = cityArr, availCapacity = weightGood, totalCapacity=weightGood, unitPriceUsd = unitPrice)
    newTrip.traveler = User.Query.get(objectId=cUser.objectId)
    try:
        newTrip.save()
    except KeyError:
        pass
    #pub_date = ''
    #travelerUser = ''
    departDate = ''
    destLocation = ''
    oriLocation = ''
    #availCapacity = ''
    try:
        #pub_date = newTrip.createdAt
        #travelerId  = newTrip.traveler.objectId
        departDate = newTrip.departureDate
        destLocation = newTrip.toLocation
        oriLocation = newTrip.fromLocation
        #availCapacity = newTrip.availCapacity
    except AttributeError:
        pass
    
    newtripDict = { 'departDate':departDate, 
                'destLocation':destLocation, 'oriLocation':oriLocation,}
    return newtripDict

def tripRequest(cUser, reqView, key):
    alert={}
    tripnow = trip.Query.get(objectId=key)
    numReq = trequests.Query.filter(Requester=cUser, tripId=tripnow).count()
    print numReq#remove
    try:
        if cUser.objectId == tripnow.traveler.objectId:
            alert['text'] = "Buddy, you can't own the penthouse and lease it to yourself, yeah ? =D !"
            alert['type'] = "warning"
            return alert
        elif numReq>0:
            alert['text'] = "You can't request more than once ;)"
            alert['type'] = "warning"
            return alert     
    except AttributeError:
        pass
    try:

        deliveryCity = tripnow.toLocation
        item_name = reqView.cleaned_data['item_name']
        item_price = reqView.cleaned_data['item_price']
        item_quantity = reqView.cleaned_data['item_quantity']
        shop_name = reqView.cleaned_data['shop_name']
        weightGood = reqView.cleaned_data['weightGood']
        item_description = reqView.cleaned_data['comments']

        newRequest = trequests(moreInfo=item_description, weightRequested=weightGood, deliveryCity=deliveryCity, accepted=False,
                        paymentStatus=False, deliveryStatus=False)
        
        newRequest.tripId = tripnow
        newRequest.Requester = cUser
        newRequest.save()
        #items_total_price = priceCalc(item_quantity, item_price) 
        new_item = Item(name=item_name, quantity=item_quantity, description=item_description, unitPrice=item_price)
        new_item.request = newRequest
        new_item.save()
        print newRequest

    except AttributeError:
        newRequest=''
        # alerts in case try does not go true
        alert['text'] = 'Request not submitted. Try again...'
        alert['type'] = 'warning'
        pass
    if newRequest:
        alert = {'text':'Request submitted with success. You will be notified as soon as Traveler accept it.','type':'success'}
 
    return alert

def isodate_to_tz_datetime(isodate):
    """
    Convert an ISO date string 2011-01-01 into a timezone aware datetime that
    has the current timezone.
    """
    date = datetime.datetime.strptime(isodate, '%m-%d-%Y')
    current_timezone = timezone.get_current_timezone()
    return current_timezone.localize(date, is_dst=None)
def priceCalc(weight, distance):
    price = weight * distance
    price = Money(amount=price,currency='USD')
    return str(price)