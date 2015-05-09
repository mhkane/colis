from django.shortcuts import render
from signup.schemes import is_logged_in, User, handle_uploaded_file, sign_in,\
    change_password
    
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from trips.forms import addForm, editproForm, reviewForm
from trips.crtrips import tripCreate
from trips.crtrips import trip
from account.actions import request as trequests, getdeal, ref_create,\
    tripReview, get_profile_pic, get_user_info
from trips.views import fbPicture
from parse_rest.installation import Push
from account.forms import referralForm, settings_form_general,\
    settings_form_picture, settings_form_password
from parse_rest.query import QueryResourceDoesNotExist
from signup.backend_parse import reviews, Item
from parse_rest.core import ResourceRequestNotFound
from texto_airspress.schemes import auth_client, create_conversation
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
                travel_user_dic['picture']=get_profile_pic(travelUser.objectId)
                req_user_dic['picture']=get_profile_pic(reqUser.objectId)
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
            messaging_token = auth_client(cUser.objectId, 'deals', key)
            members_list = [reqUser.objectId, travelUser.objectId]
            deal_id = key # in fact it's the trip request objectId 
            checker = create_conversation(deal_id, members_list)
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
                      {'dealInfo':reqAccepted,'reqUser':req_user_dic, 'firebase_node':checker+"/"+key,
                        'travelUser':travel_user_dic,'review_form':review_form,
                        'myPicture':get_profile_pic(cUser.objectId),'greetings':cUser.username,'current_user_id':cUser.objectId,
                        'firebase_token':messaging_token,'reviews':reviews_dict,'requested_items':items_dict, 'rqkey':key})
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
        any_user_id=''
        screen_name=''
        pPicture=''
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
        chat_token=''
        try:
            anyUser = User.Query.get(username=key)
            any_user_id = anyUser.objectId
            pPicture = get_profile_pic(anyUser.objectId)
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
            screen_name = anyUser.screenName
        except (AttributeError, QueryResourceDoesNotExist):
            pass
        if not anyRating:
            anyRating = 0
        
        if anyName == cUser.username :
            is_cuser = True
        else:
            # Bring in the instant chat
            # source_id is used as a unique idenifier of conversation
            source_id = cUser.objectId + "-"+any_user_id
            chat_token = auth_client(cUser.objectId, "chat", source_id)
            chat_node = create_conversation(source_id, [cUser.objectId, any_user_id], "direct_messaging")
         
        # crunch down the long usernames; this is the sick messy way
        # we can implement the slick Messi way afterwards ;-)
        for delim in ['.','@','_']:
            if delim in anyName:
                crunch_name =''
                crunch_name += anyName
                crunch_name = crunch_name.split(delim, 1)[0]
        
        
        # let's get everything in a dict object
        proDict={'username':anyName, 'short_username':crunch_name, 'screen_name':screen_name,'is_verified':is_verified, 'is_cuser':is_cuser, 'email':anyMail, 'Bio':anyBio, 
                 'rating':anyRating, 'total_deliveries':total_deliveries, 'total_orders':total_orders, 'pPicture':pPicture,
                 'total_reviews':total_reviews, 'reviews':reviews_dict}
        referral_form = referralForm()
        if request.is_ajax():
            return render(request, 'trips/modals.html', {'userinfo':proDict, 'greetings':cUser.username, 
                                                         'myPicture':get_profile_pic(cUser.objectId)})
        context_dic = {'userinfo':proDict, 'greetings':cUser.username,
                        'myPicture':get_profile_pic(cUser.objectId), 'referral_form':referral_form}
        context_dic['firebase_token']=chat_token
        context_dic['firebase_node']=chat_node+"/"+source_id
        context_dic['current_user_id'] = cUser.objectId
        return render(request, 'account/profile.html', context_dic)
    return HttpResponseRedirect(reverse('signup:index'))
                
def edit_profile(request, section):#todo last man standing
    cUser = is_logged_in(request)
    if cUser:
        proDict = get_user_info(cUser, request, user_id=cUser.objectId)
        saken = request.session['lsten']
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            context_dic={}
            if section == 'general':
                general_form = settings_form_general(request.POST)
                profile_picture_form = settings_form_picture(request.POST, request.FILES)
                if general_form.is_valid():
                    cUser.screenName = general_form.cleaned_data['screen_name']
                    cUser.timeZone = general_form.cleaned_data['time_zone']
                    cUser.save()
                else:
                    print general_form.errors  
                if profile_picture_form.is_valid():
                    profile_picture = handle_uploaded_file(request.FILES['profile_picture'], cUser)
                else:
                    print profile_picture_form.errors
                    
                # In case of profile modification we get rid of the "cached" user info
                if general_form.is_valid() or profile_picture_form.is_valid():
                    try:
                        del request.session['userinfo']
                    except:
                        pass
                context_dic = {'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId), 
                                'userinfo':proDict,'general_form':general_form,'pic_form':profile_picture_form}
                context_dic['password_form']=settings_form_password()
                context_dic['tab_general']="active in"
                    
            elif section == 'security':
                password_form = settings_form_password(request.POST)
                context_dic = {'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId), 
                                'userinfo':proDict}
                if password_form.is_valid():
                    current_password = password_form.cleaned_data['current_pass'] 
                    test_user = sign_in(request, login_dic={'username':cUser.username,
                                                            'password':current_password})
                    try:
                        user_id = test_user.objectId
                        new_password = password_form.clean_new_pass_conf()
                        if new_password:
                            change_password(new_password, user_id)
                    except(AttributeError):
                        context_dic['alert']=test_user
                context_dic['password_form']=password_form
                context_dic['general_form'] = settings_form_general()
                context_dic['pic_form']=settings_form_picture()
                context_dic['tab_security']="active in"
            return render(request, 'account/editprofile.html', context_dic )        
                          
        else:
            general_form = settings_form_general()
            profile_picture_form = settings_form_picture()
            password_form = settings_form_password()
            context_dic = {'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId), 
                           'userinfo':proDict,'general_form':general_form,'tab_general':'active in',
                            'pic_form':profile_picture_form, 'password_form':password_form}
            return render(request, 'account/editprofile.html', context_dic )
    
    return HttpResponseRedirect(reverse('signup:index'))
            
    
def referral(request):
    cUser = is_logged_in(request)
    alert = {}
    if cUser:
        context_dic = {'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId)}
        if request.method =='POST':
            referralView = referralForm(request.POST)
            if referralView.is_valid():
                alert = ref_create(referralView, cUser, request)
            else:
                print referralView.errors
            pro_dic = get_user_info(cUser, request, user_id=cUser.objectId)
            context_dic['userinfo']=pro_dic
            context_dic['alert']=alert
            context_dic['referral_form']=referralView
            context_dic['tab_friends']='active in'  
            return render(request,'account/profile.html', context_dic)#we probably won't use this template but a child-template
        else:
            referralView = referralForm()
            context_dic['alert']=alert
            context_dic['referral_form']=referralView
            return render(request, 'account/profile.html', context_dic)
    return HttpResponseRedirect(reverse('signup:index'))
    
                            