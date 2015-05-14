from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from signup.schemes import User #ParseUser
from trips.crtrips import trip, tripFind, tripRequest
from signup.schemes import is_logged_in
from trips.forms import searchForm, requestForm
from string import split
from account.actions import get_profile_pic
from datetime import datetime


def fbPicture(request):
    try:
        pPicture = request.session['pPicture']
    except:
        pPicture=''
    return pPicture
def activeTrips(request):
    cUser = is_logged_in(request)
    if cUser:
        myPicture = fbPicture(request) or get_profile_pic(cUser.objectId)
        allTrips = trip.Query.filter(departureDate__gte=datetime.now()).order_by("-createdAt")
        page_one = allTrips.limit(10)
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
                    destCity = areas_dest_location[0]
                    oriCountry = areas_ori_location[-1]
                    oriCity = areas_ori_location[0]
                    tripDict['objTrip'+str(k)] = {'pub_date':pub_date, 
                                'travelerUser':travelerUser, 'travelerRating':user_rating,
                                'departDate':{'month':departDate.strftime("%B"), 'day':departDate.day},
                                'destLocation':{'city':destCity,'country':destCountry}, 
                                'oriLocation':{'city':oriCity,'country':oriCountry}, 
                                'available':available_weight,'total':total_weight,
                                'unit_price':unit_price,'tripId':tripId, 'pPicture':pPicture,}
                    #once the context dict created we can use render()
                    print(tripDict)
                    print k
        #Preparing search form on page
        if request.method == 'POST':
            searchView = searchForm(request.POST)
            if searchView.is_valid():
                pass
            else:
                print searchView.errors
                
        else:
            searchView = searchForm()
            
        return render(request, 'trips/voyage.html', {'tripDict':tripDict,'greetings':cUser.username, 
                                                     'myPicture':get_profile_pic(cUser.objectId),'searchForm':searchView})
    return HttpResponseRedirect(reverse('signup:index'))

def searchTrips(request):
    '''
    Generate results page 
    or just a page that look like the 'activeTrips' one.
    '''
    tripDict={}
    cUser = is_logged_in(request)
    if cUser:
        myPicture = get_profile_pic(cUser.objectId)
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            searchView = searchForm(request.POST)
            if searchView.is_valid():
                tripDict = tripFind(request, cUser, searchView)
                print tripDict
        #Preparing search form on page
            else:
                print searchView.errors
            return render(request, 'trips/voyage.html', {'tripDict':tripDict,'greetings':cUser.username, 
                                                         'searchForm':searchView,'myPicture':myPicture})             
        else:
            searchView = searchForm()
    else:
        HttpResponseRedirect(reverse('signup:index'))
            
    return HttpResponseRedirect(reverse('trips:index'))

def requestTrip(request, key):
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        myPicture = get_profile_pic(cUser.objectId)
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            reqView = requestForm(request.POST)
            if reqView.is_valid():
                alert = tripRequest(cUser, reqView, key)
                print alert
        
            else:
                print reqView.errors
            return render(request, 'trips/modals.html', {'key':key,'alert':alert,'greetings':cUser.username, 'requestForm':reqView, 'pPicture':myPicture})             
        else:
            reqView = requestForm()
    else:
        return HttpResponseRedirect(reverse('signup:index'))
    return render(request, 'trips/modals.html', {'key':key,'greetings':cUser.username, 'requestForm':reqView})
