from django.shortcuts import render
from signup.schemes import is_logged_in, User, handle_uploaded_file
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from trips.forms import addForm, editproForm
from trips.crtrips import tripCreate
from trips.crtrips import trip
from account.actions import request as trequests, getdeal
from trips.views import fbPicture
# Create your views here.
def addTrip(request):
    '''
    Create a trip in the database, render a page with a list of added trips
    '''
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            addView = addForm(request.POST)
            if addView.is_valid():
                alert = tripCreate(request, cUser, addView)
                print alert
                alert['type']='success'
                alert['text']='Trip has been successfuly registered. Requests will be coming in no time!'
        #Preparing search form on page
            else:
                print addView.errors
                alert['type']='error'
                alert['text']='Correct the information you entered. Some fields have errors..'
            return render(request, 'trips/addtrip.html', {'alert':alert,'greetings':cUser.username, 'addForm':addView})             
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
                reqIdo = anyReq.objectId
                optionBtn = 'View Details'
                if anyReq.accepted:
                    optionBtn='Go to payment'
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
                 'availCap':availCap, 'traveler':traveler, 'reqIdo':reqIdo, 'optionBtno':optionBtn}
        return render(request, 'trips/mytrips.html', {'reqTrips':reqTrips,'greetings':cUser.username,})
    return HttpResponseRedirect(reverse('signup:index'))    
                
def deals(request, key):
    '''
    When a request is accepted a deal page can be accessed where users can see each other contact info
    and confirm delivery and pay for the transaction via a Paypal payment button; this is the "View Details".
    '''
    reqAccepted = {}
    cUser = is_logged_in(request)
    if cUser:
        aRequest = trequests.Query.get(objectId=key)
        reqWeight = ''
        travelUser=''
        istraveler = False
        try:
            ## Traveler
            travelUser = aRequest.tripId.traveler
            ## Requester
            reqUser = aRequest.Requester
            ##
            aTrip = aRequest.tripId
            availCap = aRequest.tripId.availCapacity
            reqWeight = aRequest.weightRequested
        except AttributeError:
            pass#return render(request, 'trips/modals.html', {'alert':{'text':'This request does not exist !', 'type':'warning'}})
        if travelUser:
            if travelUser.objectId == cUser.objectId :
                istraveler = True
                try:
                    if not aRequest.accepted:
                        aRequest.accepted= True
                        aRequest.tripId.availCapacity =  availCap - reqWeight
                        aRequest.save()
                except AttributeError:
                    pass
                reqAccepted= getdeal(travelUser, aRequest, aTrip)
                reqAccepted['istraveler']=istraveler

                return render(request, 'trips/modals.html',{'dealInfo':reqAccepted, 'rqkey':key})            
                
            elif reqUser.objectId == cUser.objectId:
                reqAccepted= getdeal(travelUser, aRequest, aTrip)
                reqAccepted['istraveler']=istraveler
                return render(request, 'trips/modals.html',{'dealInfo':reqAccepted, 'rqkey':key})
            else:
                return HttpResponseForbidden() 
    return HttpResponseRedirect(reverse('signup:index'))      

def otRequests(request):
    k=0
    reqTrips = {}
    cUser = is_logged_in(request)
    if cUser:
        ReqObj = trequests.Query.filter(Requester=cUser)
        for anyReq in ReqObj :
                k = k + 1
                optionBtn = 'Accept'
                if anyReq.accepted:
                    optionBtn='View Details'
                pub_date = ''
                departDate = ''
                destLocation = ''
                oriLocation = ''
                availCap = ''
                reqWeight = ''
                requester = ''
                reqId=''
                try:
                    pub_date = anyReq.createdAt
                    departDate = anyReq.tripId.departureDate.date()
                    destLocation = anyReq.tripId.toLocation
                    oriLocation = anyReq.tripId.fromLocation
                    reqWeight = anyReq.weightRequested
                    requester = anyReq.Requester.username
                    availCap = anyReq.tripId.availCapacity
                    reqId= anyReq.objectId
                except AttributeError:
                    pass
            
                reqTrips['objTrip'+str(k)] = {'pubdate':pub_date, 
                 'depDate':departDate, 'cityDep':destLocation, 
                 'cityArr':oriLocation,'requestWeight':reqWeight, 
                 'availCap':availCap, 'requester':requester, 'reqId':reqId, 'optionBtn':optionBtn}
        return render(request, 'trips/mytrips.html', {'otRequest':reqTrips,'greetings':cUser.username,})
    return HttpResponseRedirect(reverse('signup:index'))    
           
def profileView(request, key):
    cUser = is_logged_in(request)
    if cUser:
        pPicture = fbPicture(request)
        anyUser = User.Query.get(username=key)
        anyName = ''
        anyMail = ''
        anyBio = ''
        anyRating = ''
        try:
            anyName = anyUser.username
            anyMail = anyUser.email
            anyBio = anyUser.userBio
            anyRating = anyUser.userRating
        except AttributeError:
            pass
        proDict={'username':anyName, 'email':anyMail, 'Bio':anyBio, 'rating':anyRating, 'pPicture':pPicture}
        if request.is_ajax():
            return render(request, 'trips/modals.html', proDict)
        return render(request, 'account/profile.html', proDict)
    return HttpResponseRedirect(reverse('signup:index'))
                
def editProfile(request):#todo last man standing
    editDict={}
    cUser = is_logged_in(request)
    if cUser:
        saken = request.session['lsten']
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            editView = editproForm(request.POST, request.FILES)
            if editView.is_valid():
                editDict = tripCreate(request, cUser, editView)
                profilePic = handle_uploaded_file(request.FILES['profilePic'], saken)
                print editDict
        #Preparing search form on page
            else:
                print editView.errors
            return render(request, 'trips/addtrip.html', {'editDict':editDict,'greetings':cUser.username, 'editproForm':editView})             
        else:
            editView = editproForm()
    else:
        return HttpResponseRedirect(reverse('signup:index'))
            
    return render(request, 'trips/addtrip.html', {'greetings':cUser.username, 'addForm':editView})
            