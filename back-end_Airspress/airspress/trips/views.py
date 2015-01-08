from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from signup.schemes import User, currentUser#ParseUser
from trips.crtrips import trip, tripFind
from signup.schemes import is_logged_in
from trips.forms import searchForm
#
#
#    Current = User.login_auth(auth_data)
#Tripy = trip(departureDate=  , fromLocation= , text=  , toLocation= )
#Tripy.traveler = CurrentUser

def activeTrips(request):
    cUser = is_logged_in(request)
    if cUser:
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
            
        return render(request, 'trips/voyage.html', {'tripDict':tripDict,'greetings':cUser.username, 'searchForm':searchView})
    return HttpResponseRedirect(reverse('signup:index'))

def searchTrips(request):
    '''
    Generate results page 
    or just a page that look like the 'activeTrips' one.
    '''
    tripDict={}
    cUser = is_logged_in(request)
    if cUser:
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            searchView = searchForm(request.POST)
            if searchView.is_valid():
                tripDict = tripFind(request, cUser, searchView)
                print tripDict
        #Preparing search form on page
            else:
                print searchView.errors
            return render(request, 'trips/voyage.html', {'tripDict':tripDict,'greetings':cUser.username, 'searchForm':searchView})             
        else:
            searchView = searchForm()
    else:
        HttpResponseRedirect(reverse('signup:index'))
            
    return HttpResponseRedirect(reverse('trips:index'))
