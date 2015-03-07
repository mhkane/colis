from django.shortcuts import render
from signup.schemes import is_logged_in, User, handle_uploaded_file
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from trips.forms import addForm, editproForm
from trips.crtrips import tripCreate
from trips.crtrips import trip
from account.actions import request as trequests, getdeal, ref_create
from trips.views import fbPicture
from parse_rest.installation import Push
from account.forms import referralForm
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
    "key" identify the deal page with a unique link e.g. "airspress.com/account/deals/uY45Egr"
    where "key" is "uY45Egr"
    '''
    reqAccepted = {}
    cUser = is_logged_in(request)
    if cUser:
        aRequest = trequests.Query.get(objectId=key)
        reqWeight = ''
        travelUser=''
        reqUser=''
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
            pass
            #return render(request, 'trips/modals.html', {'alert':{'text':'This request does not exist !', 'type':'warning'}})
        if travelUser and reqUser:
            #who is visiting the deal page ?
            if travelUser.objectId == cUser.objectId :
                #if it is traveler we set some context variable for templates
                istraveler = True
                #and we push a notification for a first visit which is equivalent 
                #to clicking on "accept" button
                try:
                    if not aRequest.accepted:
                        aRequest.accepted= True
                        push_alert = travelUser.username + ' accepted your request!'
                        Push.alert({"alert": push_alert,
                                 "badge": "Increment"}, where={"appUser":{"__type":"Pointer","className":"_User","objectId":reqUser.objectId}})
                        aRequest.tripId.availCapacity =  availCap - reqWeight
                        aRequest.save()
                except AttributeError:
                    pass
                # getdeal get the deal class object associated with the request 
                reqAccepted= getdeal(travelUser, aRequest, aTrip)
                reqAccepted['istraveler']=istraveler
                # reqAccepted dict contains all specific info for the deal 
                print reqAccepted
                return render(request, 'trips/modals.html',{'dealInfo':reqAccepted, 'rqkey':key})            
                
            elif reqUser.objectId == cUser.objectId:
                reqAccepted= getdeal(travelUser, aRequest, aTrip)
                reqAccepted['istraveler']=istraveler
                try:
                    if not aRequest.accepted:
                        reqAccepted['isaccepted']=False
                except AttributeError:
                    pass
                return render(request, 'trips/modals.html',{'dealInfo':reqAccepted, 'rqkey':key})
            else:
                return HttpResponseForbidden() 
    return HttpResponseRedirect(reverse('trips:index')) # We aren't redirecting to signup:index to avoid a certain lag on signup page

def otRequests(request):
    k=0
    reqTrips = {}
    cUser = is_logged_in(request)
    if cUser:
        his_trips = trip.Query.filter(traveler=cUser)
        ReqObj = trequests.Query.filter(tripId__in=his_trips)
        for anyReq in ReqObj :
                k = k + 1
                optionBtn = 'Accept'
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
                    if anyReq.accepted:
                        optionBtn='View Details'
                except AttributeError:
                    pass
                if reqId:
                    reqTrips['objTrip'+str(k)] = {'pubdate':pub_date, 
                     'depDate':departDate, 'cityDep':destLocation, 
                     'cityArr':oriLocation,'requestWeight':reqWeight, 
                     'availCap':availCap, 'requester':requester, 'reqId':reqId, 'optionBtn':optionBtn}
                print reqTrips
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
        proDict={'greetings':anyName,'username':anyName, 'email':anyMail, 'Bio':anyBio, 'rating':anyRating, 'pPicture':pPicture}
        if request.is_ajax():
            return render(request, 'trips/modals.html', proDict)
        return render(request, 'account/profile.html', proDict)
    return HttpResponseRedirect(reverse('signup:index'))
                
def editProfile(request):#todo last man standing
    cUser = is_logged_in(request)
    if cUser:
        saken = request.session['lsten']
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            editView = editproForm(request.POST, request.FILES)
            if editView.is_valid():
                
                profilePic = handle_uploaded_file(request.FILES['profilePic'], saken)
                
        #
            else:
                print editView.errors
            return render(request, 'trips/editprofile.html', {'greetings':cUser.username, 'editproForm':editView})             
        else:
            editView = editproForm()
            return render(request, 'trips/editprofile.html', {'greetings':cUser.username, 'addForm':editView})
    
    return HttpResponseRedirect(reverse('signup:index'))
            
    
def referral(request):
    cUser = is_logged_in(request)
    alert = {}
    if cUser:
        if request.method =='POST':
            referralView = referralForm(request.POST)
            if referralView.is_valid():
                alert = ref_create(referralView,cUser)
            else:
                print referralView.errors
            return render(request,'account/profile.html',{'alert':alert, 'referForm':referralView})#we probably won't use this template but a child-template
        else:
            referralView = referralForm()
            return render(request, 'account/profile.html',{'referForm':referralView, 'alert': alert})
    return HttpResponseRedirect(reverse('signup:index'))
    
                            