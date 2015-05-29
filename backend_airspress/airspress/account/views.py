from django.shortcuts import render
from signup.schemes import is_logged_in, User, handle_uploaded_file, sign_in,\
    change_password
    
from django.http.response import HttpResponseRedirect, HttpResponseForbidden,\
    HttpResponseBadRequest, HttpResponseNotFound, HttpResponse
from django.core.urlresolvers import reverse
from trips.forms import addForm, reviewForm
from trips.crtrips import tripCreate
from trips.crtrips import trip
from account.actions import request as trequests, getdeal, ref_create,\
    tripReview, get_profile_pic, get_user_info, notify, total_deal_price
from account.forms import referralForm, settings_form_general,\
    settings_form_picture, settings_form_password
from parse_rest.query import QueryResourceDoesNotExist
from signup.backend_parse import review, Item, Notifications
from parse_rest.core import ResourceRequestNotFound
from texto_airspress.schemes import auth_client, create_conversation,\
    retrieve_conversation
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import ensure_csrf_cookie
from account.schemes import get_notifications
# Create your views here.
def addTrip(request):
    '''
    Create a trip in the database, render a page with a list of added trips
    '''
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        context_dict = {}
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            addView = addForm(request.POST)
            if addView.is_valid():
                alert = tripCreate(request, cUser, addView)
                print alert
                if alert:
                    alert = {}
                    alert['type']='success'
                    alert['text']='Trip has been successfuly registered. Requests will be coming in no time!'
        #Preparing search form on page
            else:
                print addView.errors
                alert['type']='danger'
                alert['text']='Correct the information you entered. Some fields have errors..'
            context_dict.update({'alert':alert,'greetings':cUser.username, 'addForm':addView})    
            return render(request, 'trips/addtrip.html', context_dict)             
        else:
            addView = addForm()
    else:
        return HttpResponseRedirect(reverse('signup:index'))
    context_dict.update({'greetings':cUser.username, 'addForm':addView})        
    return render(request, 'trips/addtrip.html', context_dict)

def myTrips(request, key):
    '''
    
    '''
    k=0
    ownTrips = {}
    try:
        aUser = User.Query.get(username=key)
    except:
        return HttpResponseBadRequest() 
    cUser = is_logged_in(request)
    if cUser:
        TripObj = trip.Query.filter(traveler=aUser).order_by('createdAt')
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
        
        context_dict = {'ownTrips':ownTrips,'greetings':cUser.username,
                         'myPciture':get_profile_pic(cUser.objectId)}
        
        
        
        return render(request, 'trips/mytrips.html', context_dict)
    return HttpResponseRedirect(reverse('signup:index'))

def requestedTrips(request):
    '''
    
    '''
    k=0
    reqTrips = {}
    cUser = is_logged_in(request)
    if cUser:
        try:
            ReqObj = trequests.Query.filter(Requester=cUser)
            
            for anyReq in ReqObj :
                    reqIdo = anyReq.objectId
                    optionBtn = 'View Details'
                    status ={'type':'warning','text':"Pending Approval"}
                    
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
                        if anyReq.accepted:
                            optionBtn='View AirDeal'
                            status = {'type':'success','text':'In Progress'}
                        if anyReq.completed:
                            status = status = {'type':'success','text':"Completed"}   
                    except AttributeError:
                        pass
                    reqTrips['objTrip'+str(k)] = {'pubdate':pub_date, 
                     'depDate':departDate, 'cityDep':destLocation, 
                     'cityArr':oriLocation,'requestWeight':reqWeight, 
                     'availCap':availCap, 'traveler':traveler, 'reqId':reqIdo,
                      'optionBtn':optionBtn, 'status':status}
        except: 
            pass
        
        context_dict = {'traveler':False,'request_trips':reqTrips,'greetings':cUser.username,
        'myPicture':get_profile_pic(cUser.objectId)}
        
                  
        return render(request, 'trips/in_out_requests.html', context_dict)
    return HttpResponseRedirect(reverse('signup:index'))    

def otRequests(request):
    k=0
    reqTrips = {}
    cUser = is_logged_in(request)
    if cUser:
        try:
            his_trips = trip.Query.filter(traveler=cUser)
        except QueryResourceDoesNotExist:
            pass
        try:
            ReqObj = trequests.Query.filter(tripId__in=his_trips)
            for anyReq in ReqObj :
                    k = k + 1
                    optionBtn = 'View Details'
                    pub_date = ''
                    departDate = ''
                    destLocation = ''
                    oriLocation = ''
                    availCap = ''
                    reqWeight = ''
                    requester = ''
                    reqId=''
                    status ={'type':'warning','text':"Pending Approval"}
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
                            optionBtn='View AirDeal'
                            status = {'type':'success','text':'In Progress'}
                        if anyReq.completed:
                            status = status = {'type':'success','text':"Completed"}     
                    except AttributeError:
                        pass
                    if reqId:
                        reqTrips['objTrip'+str(k)] = {'pubdate':pub_date, 
                         'depDate':departDate, 'cityDep':destLocation, 
                         'cityArr':oriLocation,'requestWeight':reqWeight, 
                         'availCap':availCap, 'requester':requester, 'reqId':reqId, 
                         'optionBtn':optionBtn, 'status':status}
                    print reqTrips
        except (AttributeError, QueryResourceDoesNotExist):
            pass
        context_dict = {'traveler':True,'request_trips':reqTrips,'greetings':cUser.username,
                         'myPicture':get_profile_pic(cUser.objectId)}
        
        
        return render(request, 'trips/in_out_requests.html', context_dict)
    return HttpResponseRedirect(reverse('signup:index'))

#some views share a lot of context with this one
# so i ended up placing some hooks to catch the signal hehe.
# Hence external_alert and other external_* are totaly useless to
# the view by itself, they just serve as hooks for other "children" views(there is not really such thing
# as a children view, i'm just "talking with pictures" here) .                
def deals(request, key, external_alert={}, external_context=False):
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
        travelUser=''
        reqUser=''
        try:
            ## Traveler
            travelUser = aRequest.tripId.traveler
            ## Requester
            reqUser = aRequest.Requester
            ##
            aTrip = aRequest.tripId
            
        except AttributeError:
            return HttpResponseNotFound()
            
        if travelUser and reqUser:
            #creating a dict object that will be used in templates
            travel_user_dic = {'username':travelUser.username}
            req_user_dic = {'username':reqUser.username}
           
            travel_user_dic['picture']=get_profile_pic(travelUser.objectId)
            req_user_dic['picture']=get_profile_pic(reqUser.objectId)
            
            #  get the deal info associated with the airdeal request 
            reqAccepted= getdeal(travelUser, reqUser, aRequest, aTrip)
            
            # who is visiting the deal page ?
            if travelUser.objectId == cUser.objectId :
                
                reqAccepted['istraveler']=True
                # reqAccepted dict contains all specific info for the deal 
                print reqAccepted 
                
                # decrement notifications counter 
                notif_traveler = getattr(aRequest,'notifTraveler',False)
                if notif_traveler:
                    aRequest.notifTraveler = 0
                    aRequest.save()       
                    try:
                        if cUser.notifications:
                            cUser_notif = Notifications.Query.get(targetUser = cUser.objectId)
                            cUser_notif.notifInDeals -= 1
                            cUser_notif.save()
                    except AttributeError:
                        pass
            elif reqUser.objectId == cUser.objectId:
                
                reqAccepted['istraveler']= False
                # decrement notifications counter
                notif_requester = getattr(aRequest,'notifRequester',False)
                if notif_requester:
                    aRequest.notifRequester = 0
                    aRequest.save()
                    try:
                        if cUser.notifInDeals:
                            cUser_notif = Notifications.Query.get(targetUser = cUser.objectId)
                            cUser_notif.notifOutDeals -= 1
                            cUser_notif.save()
                    except AttributeError:
                        pass
                
            else:
                return HttpResponseForbidden()
            print reqAccepted 
            #if everything so far is ok and nothing forbidden
            # we fetch the conversations between the 2 users
            # on this deal
            messaging_token = auth_client(cUser.objectId, 'deals', key)
            members_list = [reqUser.objectId, travelUser.objectId]
            deal_id = key # in fact it's the trip request objectId 
            chat_node = create_conversation(deal_id, members_list)
            # items to purchase on this deal
            wanted_items = Item.Query.filter(request=aRequest)
            k=0
            items_dict={}
            for wanted_item in wanted_items:
                try:
                    k=k+1
                    items_dict['item'+str(k)]= {'name':getattr(wanted_item,'name',''),'type':getattr(wanted_item,'type','None'),
                                           'unitPrice':getattr(wanted_item, 'unitPrice',0.00),'quantity':getattr(wanted_item,'quantity',1), 
                                           'price':getattr(wanted_item,'price','0.00')}
                    print items_dict
                except (AttributeError,QueryResourceDoesNotExist):
                    pass
            total = total_deal_price(items_dict,reqAccepted.get('commission',0.00))
            reqAccepted['total_price'] = total
            # reviews on this deal
            deal_reviews = review.Query.filter(reviewedRequest=aRequest)
            reviews_dict = {}
            k=0
            for deal_review in deal_reviews:
                try:
                    k=k+1
                    reviews_dict['review'+str(k)] = {'sender':{'name':deal_review.reviewer.username,
                                'picture':get_profile_pic(deal_review.reviewer.objectId)},'text':deal_review.reviewText,
                                'rating':deal_review.rating,'pubDate':deal_review.createdAt.date()}  
                except (AttributeError, QueryResourceDoesNotExist):
                    pass  
            
            
            review_form = reviewForm()
            #if not reqAccepted:
            #     return Http404()
            #decrement on deal
            notif_dict = get_notifications(cUser.objectId)
            context_dic = {'alert':external_alert,'dealInfo':reqAccepted,'reqUser':req_user_dic, 
                           'firebase_node':chat_node+"/"+key,'travelUser':travel_user_dic,'review_form':review_form,
                        'myPicture':get_profile_pic(cUser.objectId),'greetings':cUser.username,
                        'current_user_id':cUser.objectId,
                        'firebase_token':messaging_token,'reviews':reviews_dict,'requested_items':items_dict, 'rqkey':key}
            
            return render(request, 'account/deals.html', context_dic)
    return HttpResponseRedirect(reverse('trips:index')) # We aren't redirecting to signup:index to avoid a certain lag on signup page


def accept_request(request, key):
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        try:
            this_deal = trequests.Query.get(objectId = key)
            print this_deal
            traveler = this_deal.tripId.traveler
            print traveler
            if cUser.username == traveler.username:
                
                if not getattr(this_deal,'accepted',False):
                    
                    this_deal.accepted= True
                    this_trip = this_deal.tripId
                    this_trip.availCapacity =  this_trip.availCapacity - this_deal.weightRequested
                    print 'not here'
                    this_trip.save()
                    this_deal.save()  
                    origin = traveler.Name
                    target = this_deal.Requester.Name
                    target_id = this_deal.Requester.objectId
                    email = this_deal.Requester.email
                    alert = {'type':'success', 'text':'Deal is accepted. Now it''s an Airdeal!'}
                        
                    notify(request, "accept_request",origin,target,target_id,email, link=reverse('account:deals', args=[key]))
        except AttributeError:
            alert = {'type':'danger', 'text':'There was an error with the server ...'}
        print alert    
        return render(request, 'trips/alerts.html', {'alert':alert})
    return HttpResponseRedirect(reverse('signup:index'))
def confirm_delivery(request, key):
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        try:
            this_deal = trequests.Query.get(objectId = key)
            requester = this_deal.Requester
            if cUser.username == requester.username:
                this_deal.deliveryStatus = True
                this_deal.save()
                alert = {'type':'success', 'text':'This Airdeal is marked as delivered. Please leave a review for the traveler.'}
                
        except AttributeError:
            alert = {'type':'danger', 'text':'There was an error with the server ...'}
        print alert    
        return deals(request, key, external_alert=alert)
    return HttpResponseRedirect(reverse('signup:index'))
def confirm_payment(request, key):
    alert={}
    cUser = is_logged_in(request)
    if cUser:
        try:
            this_deal = trequests.Query.get(objectId = key)
            traveler = this_deal.tripId.traveler
            if cUser.username == traveler.username:
                print 'not here'
                this_deal.paymentStatus = True
                this_deal.save()
                alert = {'type':'success', 'text':'This Airdeal is marked as paid. Please leave a review for the buyer.'}
                
        except AttributeError:
            alert = {'type':'danger', 'text':'There was an error with the server ...'}
        print alert    
        return deals(request, key, external_alert=alert)
    return HttpResponseRedirect(reverse('signup:index'))            
def reviewTrip(request,key):
    alert={}
    context_dic={}
    cUser = is_logged_in(request)
    if cUser:
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            review_form = reviewForm(request.POST)
            if review_form.is_valid():
                new_review = tripReview(cUser, review_form, key)
                if new_review:
                    context_dic['review']=new_review
                    if getattr(cUser,'totalReview',False):
                        cUser.totalReviews.increment()
                    else:
                        cUser.totalReviews = 1
                    print 'reviews work'  
                    cUser.save()
                try:
                    this_deal = trequests.Query.get(objectId=key)
                    if this_deal.purchaserReview and this_deal.travelerReview:
                        this_deal.completeStatus = True
                        this_deal.save()
                        traveler = this_deal.tripId.traveler
                        print 'traveler works'
                        if getattr(traveler,'totalDeliveries',False):
                            traveler.totalDeliveries.increment()
                        else:
                            traveler.totalDeliveries = 1
                        
                        print 'increment works'
                        requester = this_deal.Requester
                        if getattr(requester,'totalOrders',False):
                            requester.totalOrders.increment()
                        else:
                            requester.totalOrders = 1
                        requester.totalOrders.increment()
                        traveler.save()
                        requester.save()
                except AttributeError:
                    pass        
            else:
                print review_form.errors
            
            context_dic.update({'key':key,'alert':alert,'greetings':cUser.username, 
                    'review_form':review_form, 'myPicture':get_profile_pic(cUser.objectId)}) 
            
            return render(request, 'account/reviews_readonly.html', context_dic)             
        else:
            return HttpResponseRedirect(reverse('account:deals',kwargs={'key':key}))
    else:
        return HttpResponseRedirect(reverse('trips:index'))

#    
#--------------------------------------------------------------------------------------
# This is the User Profile related zone.
# Profile Edition, Profile Display and Referral are dealt with here
# Have a nice time playing with that !
# 
@ensure_csrf_cookie   
def profileView(request, key):
    cUser = is_logged_in(request)
    if cUser:
        proDict = get_user_info(cUser, request, username=key)
        any_user_id=proDict.get('id', '') or User.Query.get(username = proDict.get('username','').objectId)
        is_cuser = proDict.get('is_cuser',False)
        chat_token=''
        chat_node=''
        source_id=''
       
        
        if not is_cuser : 
            # Bring in the instant chat
            # source_id is used as a unique identifier of conversation
            # hence the use of sorting is an obvious attempt to maintain same source
            # disregarding which one of the two parties is the current user
            source_id = ''.join(sorted(cUser.objectId + "-"+any_user_id))
            chat_token = auth_client(cUser.objectId, "chat", source_id)
            chat_node = create_conversation(source_id, [cUser.objectId, any_user_id], "direct_messaging")
        
        referral_form = referralForm()
        
        if request.is_ajax():
            return render(request, 'trips/modals.html', {'userinfo':proDict, 'greetings':cUser.username, 
                                                         'myPicture':get_profile_pic(cUser.objectId)})
        context_dic = {'userinfo':proDict, 'greetings':cUser.username,
                        'myPicture':get_profile_pic(cUser.objectId), 'referral_form':referral_form}
        if chat_node:
            context_dic['firebase_token']=chat_token
            context_dic['source_id'] = source_id
            context_dic['firebase_node']=chat_node+"/"+source_id
            context_dic['current_user_id'] = cUser.objectId
        return render(request, 'account/profile.html', context_dic)
    return HttpResponseRedirect(reverse('signup:index'))
                
def edit_profile(request, section):#todo last man standing
    cUser = is_logged_in(request)
    if cUser:
        proDict = get_user_info(cUser, request, user_id=cUser.objectId)
        if request.method == 'POST': #If it's POST we'll output results no matter what, results could be errors
            context_dic={}
            if section == 'general':
                general_form = settings_form_general(request.POST)
                profile_picture_form = settings_form_picture( request.POST, request.FILES)
                if general_form.is_valid():
                    try:
                        #update on Parse
                        cUser.screenName = general_form.cleaned_data.get('screen_name', False) or cUser.screenName
                        
                        cUser.timeZone = general_form.cleaned_data.get('time_zone', False) or cUser.timeZone
                   
                    except AttributeError:
                        pass
                    cUser.save()
                    
                else:
                    print general_form.errors  
                if profile_picture_form.is_valid():
                    try:
                        profile_picture = handle_uploaded_file(profile_picture_form.cleaned_data.get('profile_picture', False), cUser)
                    except MultiValueDictKeyError:
                        pass
                else:
                    print profile_picture_form.errors
                    
                # In case of profile modification we get rid of the "cached" user info
                if general_form.is_valid() or profile_picture_form.is_valid():
                    try:
                        del request.session['userinfo']
                    except:
                        pass
                #immediately update userinfo dict
                try:
                    proDict.update({'pPicture':get_profile_pic(cUser.objectId)})
                    proDict.update({'screen_name':cUser.screenName}) 
                except AttributeError:
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
            
def inbox(request):
    cUser = is_logged_in(request)
    if cUser:
        conversations = retrieve_conversation(cUser.objectId) 
        # Nullify all inbox notifications; That's the way to do it
        #  until we choose to have message-wise status
        try:
            cUser_notif = Notifications.Query.get(targetUser=cUser.objectId)
            cUser_notif.notifInbox = 0
            cUser_notif.save()
        except (AttributeError):
            pass
        context_dic = { 'greetings':cUser.username,
                        'myPicture':get_profile_pic(cUser.objectId),
                        'conversations':conversations}
        return render(request, 'account/inbox.html', context_dic)
    return HttpResponseRedirect(reverse('signup:index'))

@ensure_csrf_cookie  
def instant_messaging(request,key):
    #key is here the username of the other party in the conversation
    #that's about how the url for instant messaging view is formatted    
    cUser = is_logged_in(request)
    
    if cUser:
        if request.method == 'POST':
            origin = request.POST.get('origin', "")
            if origin:
                text = request.POST.get('text', "")
                action = request.POST.get('action', "")
                target = request.POST.get('target', "")
                isdeal = request.POST.get('isdeal', "")
                activity_id = request.POST.get('activityId','')
                target = User.Query.get(username=target)
                origin = User.Query.get(username=origin)
                email = target.email
                if str(isdeal.lower()) == 'true':
                    notify(request, "message_deal", origin.Name, target.Name, target.objectId, email, 
                           text = text, link = action, activity_id=activity_id)
                else:
                    notify(request, "message", origin.Name, target.Name, target.objectId, email, text = text, link = action)
                return HttpResponse('success')
            return HttpResponseNotFound()
                
        else:   
            any_user_id = ''
            pPicture = ''
            try:
                any_user = User.Query.get(username=key)
                any_user_id = any_user.objectId
                pPicture = any_user.profilePicture.url   
            except (AttributeError, QueryResourceDoesNotExist):
                pass
            source_id = request.GET.get('source',False)
            # Bring in the instant chat
            # source_id is used as a unique identifier of conversation
            # hence the use of sorting is an obvious attempt to maintain same source_id
            # disregarding which one of the two parties is the current user.
            # we virtually create conversation everytime even after first creation
            # so that we don't have to check for existence
            
            if not source_id:
                source_id = ''.join(sorted(cUser.objectId + "-"+any_user_id))
            chat_token = auth_client(cUser.objectId, "chat", source_id)
            chat_node = create_conversation(source_id, [cUser.objectId, any_user_id], "direct_messaging")
            context_dic={'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId),
                         'userinfo':{'username':key,'pPicture':pPicture}}
            if chat_node:
                context_dic['firebase_token']=chat_token
                context_dic['source_id'] = source_id
                context_dic['firebase_node']=chat_node+"/"+source_id
                context_dic['current_user_id'] = cUser.objectId
            return render(request, 'account/messaging.html', context_dic)
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


        
                            