from django.shortcuts import render
from signup.schemes import is_logged_in, User
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from trips.forms import addForm
from trips.crtrips import tripCreate
from trips.crtrips import trip
from account.actions import request as trequests
# Create your views here.
def addTrip(request):
    '''
    Create a trip in the database, render a page with a list of added trips
    '''
    newtripDict={}
    cUser = is_logged_in(request)
    if cUser:
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            addView = addForm(request.POST)
            if addView.is_valid():
                newtripDict = tripCreate(request, cUser, addView)
                print newtripDict
        #Preparing search form on page
            else:
                print addView.errors
            return render(request, 'trips/addtrip.html', {'newtripDict':newtripDict,'greetings':cUser.username, 'addForm':addView})             
        else:
            addView = addForm()
    else:
        return HttpResponseRedirect(reverse('signup:index'))
            
    return render(request, 'trips/addtrip.html', {'greetings':cUser.username, 'addForm':addView})
def myTrips(request, key):
    '''
    
    '''
    k=0
    ownTrips = {}
    aUser = User.Query.get(username=key)
    cUser = is_logged_in(request)
    if cUser:
        TripObj = trip.Query.filter(traveler=aUser)
        for anyTrip in TripObj :
                k = k + 1
                pub_date = ''
                departDate = ''
                destLocation = ''
                oriLocation = ''
                availCap = ''
                totalCap = ''
                try:
                    pub_date = anyTrip.createdAt
                    departDate = anyTrip.departureDate.date()
                    destLocation = anyTrip.toLocation
                    oriLocation = anyTrip.fromLocation
                    tripId = anyTrip.objectId
                    availCap = anyTrip.availCapacity
                    totalCap = anyTrip.totalCapacity
                except AttributeError:
                    pass
            
                ownTrips['objTrip'+str(k)] = {'pubdate':pub_date, 
                 'depDate':departDate, 'cityDep':destLocation, 
                 'cityArr':oriLocation, 'availCap':availCap, 'totalCap':totalCap}
                print ownTrips
        return render(request, 'trips/mytrips.html', {'ownTrips':ownTrips,'greetings':cUser.username,})
    return HttpResponseRedirect(reverse('signup:index'))
def requestedTrips(request):
    '''
    
    '''
    k=0
    reqTrips = {}
    cUser = is_logged_in(request)
    if cUser:
        ReqObj = trequests.Query.filter(Requester=cUser)
        for anyReq in ReqObj :
                k = k + 1
                pub_date = ''
                departDate = ''
                destLocation = ''
                oriLocation = ''
                availCap = ''
                reqWeight = ''
                traveler = ''
                try:
                    pub_date = anyReq.createdAt
                    departDate = anyReq.tripId.departureDate.date()
                    destLocation = anyReq.tripId.toLocation
                    oriLocation = anyReq.tripId.fromLocation
                    reqWeight = anyReq.weightRequested
                    traveler = anyReq.tripId.traveler.username
                    availCap = anyReq.tripId.availCapacity
                except AttributeError:
                    pass
            
                reqTrips['objTrip'+str(k)] = {'pubdate':pub_date, 
                 'depDate':departDate, 'cityDep':destLocation, 
                 'cityArr':oriLocation,'requestWeight':reqWeight, 
                 'availCap':availCap, 'traveler':traveler}
        return render(request, 'trips/mytrips.html', {'ownTrips':reqTrips,'greetings':cUser.username,})
    return HttpResponseRedirect(reverse('signup:index'))    
                
def deals(request):
    '''
    When a request is accepted a deal page can be accessed where users can see each other contact info
    and confirm delivery and pay for the transaction via a Paypal payment button
    '''
    cUser = is_logged_in(request)
    if cUser:
        k=0    