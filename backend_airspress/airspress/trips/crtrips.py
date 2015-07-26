
from parse_rest.connection import register, ParseBatcher
from airspress import settings
from django.utils import timezone
import datetime
from time import strptime
from moneyed.classes import Money
from string import split
from signup.backend_parse import Item
from decimal import Decimal
from parse_rest.query import QueryResourceDoesNotExist
register(settings.APPLICATION_ID, settings.REST_API_KEY)#settings.REST_API_KEY
from parse_rest.datatypes import Object as ParseObject
from parse_rest.user import User
from account.schemes import get_profile_pic
from signup.backend_parse import request as trequests
from django.utils.translation import ugettext as _

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
    if not depDate1:
        depDate1 = timezone.now()
    else:
        depDate1 = datetime.datetime.combine(depDate1, datetime.time.min)
    if not depDate2:
        
        depDate2 = datetime.datetime.combine(depDate1 + datetime.timedelta(days=90), datetime.time.max)
    else:
        depDate2 = datetime.datetime.combine(depDate2, datetime.time.max)
    
    #Different queries depending if cities are left blank or not
    print cityDep, depDate1, depDate2#remove
    try:
        if not cityDep and not cityArr :
                allTrips = trip.Query.filter( departureDate__gte = depDate1, 
                                        departureDate__lte = depDate2).order_by('-departureDate')
        elif not cityDep:
                allTrips = trip.Query.filter( departureDate__gte = depDate1,toLocationTokens__all=process_for_search(cityArr), 
                                         departureDate__lte = depDate2).order_by('-departureDate')
        elif not cityArr:
                allTrips = trip.Query.filter( departureDate__gte = depDate1, 
                                        fromLocationTokens__all=process_for_search(cityDep), departureDate__lte = depDate2).order_by('-departureDate')
        else:
                allTrips = trip.Query.filter(fromLocationTokens__all=process_for_search(cityDep), toLocationTokens__all= process_for_search(cityArr), 
                                             departureDate__gte = depDate1, departureDate__lte = depDate2).order_by('-departureDate')
    except:
        return False
    print allTrips#remove
    count_trips = allTrips.count()
    page_one = allTrips.limit(10)
    #per_page = 10
    #cut_page = 10
    #while count_trips>0:
    #
    #    count_trips -= per_page
    #    
    
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
        available_weight = 0
        total_weight = 0
        user_rating = 0
        pPicture=''
        try:
            pub_date = anyTrip.createdAt
            travelerId  = anyTrip.traveler.objectId
            departDate = anyTrip.departureDate.date()
            destLocation = anyTrip.toLocation
            oriLocation = anyTrip.fromLocation
            tripId = anyTrip.objectId
            pPicture = get_profile_pic(travelerId)
            available_weight = anyTrip.availCapacity
            total_weight = anyTrip.totalCapacity
            traveler = User.Query.get(objectId=travelerId)
            unit_price = anyTrip.unitPriceUsd
            user_rating = traveler.userRating
        except (AttributeError, QueryResourceDoesNotExist):
            pass
        
        if travelerId:#use travelerId to access traveler info
            travelerUser = ''
            try:
                travelerUser = User.Query.get(objectId=travelerId).username.split('@')[0]
            except (AttributeError, QueryResourceDoesNotExist):
                pass
            
            if travelerUser == '':
                pass
            else:
                areas_ori_location = split(oriLocation,',') 
                areas_dest_location = split(destLocation,',')
                destCountry = areas_dest_location[-1]
                destCity = areas_dest_location[0]
                oriCountry = areas_ori_location[-1]
                oriCity = areas_ori_location[0]
                if len(areas_dest_location) > 2:
                        destCountry =  areas_dest_location[1]+ ', ' + destCountry
                if len(areas_ori_location) > 2:
                        oriCountry = areas_ori_location[1]+ ', ' + oriCountry
                tripDict['objTrip'+str(k)] = {'pub_date':pub_date, 
                'travelerUser':travelerUser, 'travelerRating':user_rating,
                'departDate':{'month':departDate.strftime("%B"), 'day':departDate.day},
                'destLocation':{'city':destCity,'country':destCountry}, 
                'oriLocation':{'city':oriCity,'country':oriCountry}, 
                'available':available_weight,'total':total_weight,
                'unit_price':unit_price,'tripId':tripId, 'pPicture':pPicture,}
                #once the context dict created we can use render()
                print(tripDict)
                print k+1
    #        cut_page += per_page    
    #       page = allTrips.skip(cut_page).limit(per_page)
    #       count_page = page.count()
    return tripDict
def tripCreate(request, cUser, addView):
    print addView.cleaned_data
    cityArr = addView.cleaned_data['cityArr']
    cityDep = addView.cleaned_data['cityDep']
    depDate = addView.cleaned_data['depDate']
    
    weightGood = addView.cleaned_data['weightGood']
    distance = addView.cleaned_data['distance']  #must be evaluated with another form field
    unitPrice = addView.cleaned_data['unit_price']#priceCalc(weightGood, distance)
    customPrice = addView.cleaned_data['custom_price']
    if customPrice:
        unitPrice =str(customPrice)
    else :
        unitPrice = unit_price_calc(distance)
            
    is_coming_back = addView.cleaned_data['return_check']
    depDate = datetime.datetime.combine(depDate, datetime.time.min)
    
    print depDate
  
    if is_coming_back:
        depart = datetime.datetime.combine(addView.cleaned_data['depDate2'], datetime.time.min)
        dep_dates = []
        dep_dates.append(depDate)
        dep_dates.append(depart)
        weight = addView.cleaned_data['weightGood2']
        weight_goods = []
        weight_goods.append(weightGood)
        weight_goods.append(weight)
        city_arr = []
        city_dep = []
        city_dep.append(cityDep)
        city_dep.append(cityArr)
        city_arr.append(cityArr)
        city_arr.append(cityDep)
        new_trips = []
        for k in range(len(dep_dates)):
            try:
                dep_date = dep_dates[k]
                weight_good = weight_goods[k]
            except:
                pass     
            try:
                city_dep_tokens = process_for_search(city_dep[k])
                city_arr_tokens = process_for_search(city_arr[k])
                # the form provided values contains states long and short names
                # We want to keep both for search engine but we don't want to store
                # the whole thing as a location so we strip the long name to only keep it
                # the tokens
                cityArr = city_arr[k].split(',')
                cityDep = city_dep[k].split(',')
                if len(cityArr) == 4:
                    cityArr.pop(2)
                if len(cityDep) == 4:
                    cityDep.pop(2)
                cityArr = ', '.join(cityArr)
                cityDep = ', '.join(cityDep)
                new_trips.append(trip(departureDate = dep_date, fromLocation = cityDep, 
                            toLocation = cityArr, availCapacity = weight_good, totalCapacity=weight_good, unitPriceUsd = unitPrice,
                            toLocationTokens = city_arr_tokens, fromLocationTokens = city_dep_tokens))
                new_trips[k].traveler = User.Query.get(objectId=cUser.objectId)
                
            except (AttributeError, KeyError, IndexError):
                pass
        batcher = ParseBatcher()
        if new_trips:
            batcher.batch_save(new_trips)
            return True
        return False
    try:
        city_dep_tokens = process_for_search(cityDep)
        city_arr_tokens = process_for_search(cityArr)
        # the form provided values contains states long and short names
        # We want to keep both for search engine but we don't want to store
        # the whole thing as a location so we strip the long name to only keep it
        # the tokens
        cityArr = cityArr.split(',')
        cityDep = cityDep.split(',')
        if len(cityArr) == 4:
            cityArr.pop(2)
        if len(cityDep) == 4:
            cityDep.pop(2)
        cityArr = ', '.join(cityArr)
        cityDep = ', '.join(cityDep)
        newTrip = trip(departureDate = depDate, fromLocation = cityDep, 
                    toLocation = cityArr, availCapacity = weightGood, totalCapacity=weightGood, unitPriceUsd = unitPrice,
                    toLocationTokens = city_arr_tokens, fromLocationTokens = city_dep_tokens)
        newTrip.traveler = User.Query.get(objectId=cUser.objectId)
    except AttributeError:
        pass
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
    had_requested = False
    try:
        tripnow = trip.Query.get(objectId=key)
        had_requested = trequests.Query.filter(Requester=cUser, tripId=tripnow)
    except (QueryResourceDoesNotExist, AttributeError):
        pass
    print had_requested#remove
    try:
        if cUser.objectId == tripnow.traveler.objectId:
            alert['text'] = _("Buddy, you can't own the penthouse and lease it to yourself, yeah ? =D !")
            alert['type'] = "warning"
            return alert
##        elif had_requested:
##            alert['text'] = _("You can't request more than once ;)")
##            alert['type'] = "warning"
##            return alert     
    except AttributeError:
        pass
    try:

        deliveryCity = tripnow.toLocation
        item_name = reqView.cleaned_data['item_name']
        item_price = price_format(reqView.cleaned_data['item_price'])
        item_quantity = reqView.cleaned_data['item_quantity']
        shop_name = reqView.cleaned_data['shop_name']
        weightGood = reqView.cleaned_data['weightGood']
        item_description = reqView.cleaned_data['comments']

        newRequest = trequests(moreInfo=item_description, weightRequested=weightGood, deliveryCity=deliveryCity, accepted=False,
                        paymentStatus=False, deliveryStatus=False)
        
        newRequest.tripId = tripnow
        newRequest.Requester = cUser
        items_total_price = priceCalc(item_quantity, item_price) 
        new_item = Item(name=item_name, quantity=item_quantity, description=item_description, unitPrice=item_price, price=items_total_price)
        newRequest.save()
        new_item.request = newRequest
        new_item.save()
        print newRequest

    except AttributeError:
        newRequest=''
        # alerts in case try does not go true
        alert['text'] = _('Request not submitted. Try again...')
        alert['type'] = 'warning'
        pass
    if newRequest:
        alert = {'text':_('Request submitted with success. You will be notified as soon as Traveler accept it.'),'type':'success'}
        
    return alert

def isodate_to_tz_datetime(isodate):
    """
    Convert an ISO date string 2011-01-01 into a timezone aware datetime that
    has the current timezone.
    """
    date = datetime.datetime.strptime(isodate, '%m-%d-%Y')
    current_timezone = timezone.get_current_timezone()
    return current_timezone.localize(date, is_dst=None)
def priceCalc(weight, unit_price):
    price = weight * Money(amount=unit_price,currency='USD')
    return str(price)
def unit_price_calc(distance):
    price = 0
    km = 1000
    max_distance = 6000*km
    groups = [1000*km, 2000*km, 4000*km, 6000*km]
    prices = [7, 10, 15, 17]
    for i in range(len(groups)-1):
        if distance < groups[i]:
            price = prices[i]
            break
        elif distance > max_distance:
            prices = groups[-1]
            break
    price = str(Money(amount=price,currency='USD'))
    digit_list = [digit for digit in price if digit.isdigit() or digit == '.']
    price = ''.join(digit_list)
    try:
        price = Decimal(price)
    except:
        price = 7        
    return str(price)
def price_format(price, currency="USD"):
    price = str(Money(amount=price,currency=currency))
    digit_list = [digit for digit in price if digit.isdigit() or digit == '.']
    price = ''.join(digit_list)
    try:
        price = Decimal(price)
    except:
        price = 0        
    return str(price)
def process_for_search(datastring):
    import re
    tokenize = lambda x: [i for i in re.findall(r'\w+', unicode(x).lower(), flags= re.UNICODE) if i]
    return tokenize(datastring)
