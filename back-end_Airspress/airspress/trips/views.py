from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from signup.schemes import User, currentUser#ParseUser
from trips.crtrips import trip, tripFind, tripRequest
from signup.schemes import is_logged_in
from trips.forms import searchForm, requestForm
#
#
#    Current = User.login_auth(auth_data)
#Tripy = trip(departureDate=  , fromLocation= , text=  , toLocation= )
#Tripy.traveler = CurrentUser
def fbPicture(request):
    pPicture = request.session['pPicture']
    return pPicture
def activeTrips(request):
    cUser = is_logged_in(request)
    if cUser:
        pPicture = request.session['pPicture']
        allTrips = trip.Query.all()
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
            pPicture = ''
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
                    tripDict['objTrip'+str(k)] = {'pub_date':pub_date, 
                    'travelerUser':travelerUser, 'departDate':departDate, 
                    'destLocation':destLocation, 'oriLocation':oriLocation, 'tripId':tripId, 'pPicture':pPicture}
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
            
        return render(request, 'trips/voyage.html', {'tripDict':tripDict,'greetings':cUser.username, 'searchForm':searchView, 'pPicture':pPicture})
    return HttpResponseRedirect(reverse('signup:index'))

def searchTrips(request):
    '''
    Generate results page 
    or just a page that look like the 'activeTrips' one.
    '''
    tripDict={}
    cUser = is_logged_in(request)
    if cUser:
        pPicture = fbPicture(request)
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            searchView = searchForm(request.POST)
            if searchView.is_valid():
                tripDict = tripFind(request, cUser, searchView)
                print tripDict
        #Preparing search form on page
            else:
                print searchView.errors
            return render(request, 'trips/voyage.html', {'tripDict':tripDict,'greetings':cUser.username, 'searchForm':searchView,'myPicture':pPicture})             
        else:
            searchView = searchForm()
    else:
        HttpResponseRedirect(reverse('signup:index'))
            
    return HttpResponseRedirect(reverse('trips:index'))

def requestTrip(request, key):
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        pPicture = fbPicture(request)
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            reqView = requestForm(request.POST)
            if reqView.is_valid():
                alert = tripRequest(cUser, reqView, key)
                print alert
        #Preparing search form on page
            else:
                print reqView.errors
            return render(request, 'trips/modals.html', {'key':key,'alert':alert,'greetings':cUser.username, 'requestForm':reqView, 'pPicture':pPicture})             
        else:
            reqView = requestForm()
    else:
        return HttpResponseRedirect(reverse('signup:index'))
    return render(request, 'trips/modals.html', {'key':key,'greetings':cUser.username, 'requestForm':reqView})