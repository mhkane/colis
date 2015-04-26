from django.shortcuts import render
from signup.schemes import is_logged_in, User, handle_uploaded_file
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from trips.forms import addForm, editproForm, reviewForm
from trips.crtrips import tripCreate
from trips.crtrips import trip
from account.actions import request as trequests, getdeal, ref_create,\
    tripReview, get_profile_pic
from trips.views import fbPicture
from parse_rest.installation import Push
from account.forms import referralForm
from parse_rest.query import QueryResourceDoesNotExist
from signup.backend_parse import reviews, Item
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
            #creating a dict object that will be used in templates
            travel_user_dic = {'username':travelUser.username}
            req_user_dic = {'username':reqUser.username}
            try:
                travel_user_dic['picture']=travelUser.profilePicture
                req_user_dic['picture']=reqUser.profilePicture
            except (AttributeError, QueryResourceDoesNotExist):
                req_user_dic['picture']=''
                travel_user_dic['picture']=''
            #  get the deal info associated with the airdeal request 
            reqAccepted= getdeal(travelUser, reqUser, aRequest, aTrip)
            # who is visiting the deal page ?
            if travelUser.objectId == cUser.objectId :
                #if it is traveler it means:
                #we must push a notification if it's a first visit 
                #( a first visit is equivalent to clicking on "accept the request" button)
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
                
                reqAccepted['istraveler']=True
                # reqAccepted dict contains all specific info for the deal 
                print reqAccepted         
                
            elif reqUser.objectId == cUser.objectId:
                reqAccepted['istraveler']= False
                try:
                    if not aRequest.accepted:
                        reqAccepted['isaccepted']=False
                except AttributeError:
                    pass
                
            else:
                return HttpResponseForbidden() 
            #if everything so far is ok and nothing forbidden
            # we fetch the conversations between the 2 users
            # on this deal
            
            # items to purchase on this deal
            wanted_items = Item.Query.filter(request=aRequest)
            k=0
            items_dict={}
            for wanted_item in wanted_items:
                try:
                    k=k+1
                    items_dict['item'+str(k)]= {'name':wanted_item.name,'type':wanted_item.type,
                                           'unitPrice':wanted_item.unitPrice,'quantity':wanted_item.quantity, 
                                           'price':wanted_item.price}
                except (AttributeError,QueryResourceDoesNotExist):
                    pass
            # reviews on this deal
            deal_reviews = reviews.Query.filter(reviewedRequest=aRequest)
            reviews_dict = {}
            k=0
            for deal_review in deal_reviews:
                try:
                    k=k+1
                    reviews_dict['review'+str(k)] = {'sender':{'name':deal_review.reviewer.username,
                                'picture':deal_review.reviewer.profilePicture},'text':deal_review.reviewText,
                                'rating':deal_review.rating,'pubDate':deal_review.createdAt.date()}  
                except (AttributeError, QueryResourceDoesNotExist):
                    pass  
            # TODO use firebase cloud functions and retrieve user_messages
            
            review_form = reviewForm()
            #if not reqAccepted:
            #     return Http404()
            return render(request, 'account/deals.html',
                      {'dealInfo':reqAccepted,'reqUser':req_user_dic,
                        'travelUser':travel_user_dic,'review_form':review_form,
                        'myPicture':get_profile_pic(cUser.objectId),'greetings':cUser.username,
                        'user_messages':'','reviews':reviews_dict,'requested_items':items_dict, 'rqkey':key})
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
def reviewTrip(request,key):
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            review_form = reviewForm(request.POST)
            if review_form.is_valid():
                new_review = tripReview(cUser, review_form, key)
                
            else:
                print review_form.errors
            return render(request, 'trips/reviews.html', 
                    {'key':key,'review':new_review,'alert':alert,'greetings':cUser.username, 
                    'reviewForm':review_form, 'myPicture':get_profile_pic(cUser.objectId)})             
        else:
            return HttpResponseRedirect(reverse('account:deals',kwargs={'key':key}))
    else:
        return HttpResponseRedirect(reverse('trips:index'))
def profileView(request, key):
    cUser = is_logged_in(request)
    if cUser:
        anyName = ''
        anyMail = ''
        anyBio = ''
        anyRating = ''
        total_reviews = 0
        total_deliveries = total_reviews
        total_orders = 0
        is_verified = ''
        is_cuser = False
        reviews_dict={}
        try:
            anyUser = User.Query.get(username=key)
            pPicture = get_profile_pic(cUser.objectId)
            anyName = anyUser.username
            anyMail = anyUser.email
            anyReview = reviews.Query.filter(reviewedUser=anyUser)
            k=0
            for review in anyReview:
                k = k+1
                reviews_dict['review'+str(k)] = {'sender':{'name':review.reviewer.username,
                                                           'picture':get_profile_pic(review.reviewer.objectId)},
                                                 'rating':review.rating,'text':review.reviewText, 'pub_date':review.createdAt.date()}
            is_verified = anyUser.emailVerified
            anyRating = anyUser.userRating
            total_reviews = anyUser.totalReviews
            total_deliveries = anyUser.totalDeliveries
            total_orders = anyUser.totalOrders
            anyBio = anyUser.userBio 
        except (AttributeError, QueryResourceDoesNotExist):
            pass
        if not anyRating:
            anyRating = 0
        
        if anyName == cUser.username :
            is_cuser = True
         
        # crunch down the long usernames; this is the sick messy way
        # we can implement the slick Messi way afterwards ;-)
        for delim in ['.','@','_']:
            if delim in anyName:
                anyName = anyName.split(delim, 1)[0]
        # let's get everything in a dict object
        proDict={'username':anyName, 'is_verified':is_verified, 'is_cuser':is_cuser, 'email':anyMail, 'Bio':anyBio, 
                 'rating':anyRating, 'total_deliveries':total_deliveries, 'total_orders':total_orders, 'pPicture':pPicture,
                 'total_reviews':total_reviews, 'reviews':reviews_dict}
        if request.is_ajax():
            return render(request, 'trips/modals.html', {'userinfo':proDict, 'greetings':cUser.username, 
                                                         'myPicture':get_profile_pic(cUser.objectId)})
        return render(request, 'account/profile.html', {'userinfo':proDict, 'greetings':cUser.username,
                                                        'myPicture':get_profile_pic(cUser.objectId)})
    return HttpResponseRedirect(reverse('signup:index'))
                
def editProfile(request):#todo last man standing
    cUser = is_logged_in(request)
    if cUser:
        saken = request.session['lsten']
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            edit_profile_form = editproForm(request.POST, request.FILES)
            if edit_profile_form.is_valid():
                
                profilePic = handle_uploaded_file(request.FILES['profilePic'], saken)
                
        #
            else:
                print edit_profile_form.errors
            return render(request, 'account/editprofile.html', {'greetings':cUser.username, 'editproForm':edit_profile_form})             
        else:
            editView = editproForm()
            return render(request, 'account/editprofile.html', {'greetings':cUser.username, 'addForm':editView})
    
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
    
                            