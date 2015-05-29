'''
Relevant models (not Django db-backed models) to handle
user actions : put request on a travel, add a trip, make payments
and also edit profile information
'''
from signup.schemes import User
from parse_rest.datatypes import Object as ParseObject, Function
from django.core.urlresolvers import reverse
from parse_rest.query import QueryResourceDoesNotExist
from decimal import Decimal
from signup.backend_parse import review, referral, trequests
from parse_rest.installation import Push
from trips.crtrips import priceCalc, price_format
from moneyed.classes import Money

class request(ParseObject):
    pass
#Cloud function for mail sending
send_mail = Function("email")
send_template = Function("emailTemplate")
# function to recover information for a given deal 
def getdeal(travelUser, reqUser, aRequest, aTrip):
    reqAccepted = {}
    try:
        #reqWeight = aRequest.weightRequested
        #priceDeal = aRequest.priceUsd
        pub_date = aRequest.createdAt
        departDate = aTrip.departureDate.date()
        destLocation = aTrip.toLocation
        oriLocation = aTrip.fromLocation
        reqAccepted['commission'] = priceCalc(getattr(aTrip,'unitPriceUsd',0.00),getattr(aRequest,'weightRequested',1))
    except AttributeError:
        pass
    reqUser_pic = ''
    traveler_pic=''
    try:
        reqUser_pic = get_profile_pic(reqUser.objectId)
        traveler_pic = get_profile_pic(travelUser.objectId)
        reqAccepted['isaccepted'] = getattr(aRequest,'accepted',False)
        reqAccepted['ispayed']= aRequest.paymentStatus
        reqAccepted['isdeliv']= aRequest.deliveryStatus
    except AttributeError:
        pass
    buyer_reviewed = True
    traveler_reviewed = True
    try:
        try:
            buyer_reviewed = aRequest.purchaserReview
        except AttributeError:
            buyer_reviewed = False    
            traveler_reviewed = aRequest.travelerReview
    except AttributeError:
        traveler_reviewed = False
    
           
    reqAccepted.update({'pubdate':pub_date,
             'depDate':departDate, 'cityDep':oriLocation, 
             'cityArr':destLocation,
             'traveler':{'username':travelUser.username,'picture':traveler_pic,'isreviewed':traveler_reviewed},
             'reqUser':{'username':reqUser.username,'picture':reqUser_pic,'isreviewed':buyer_reviewed}})
    # send notification
    print reqAccepted
    return reqAccepted

def total_deal_price(items_dict, commission):
    all_items_price = 0
    for item, content in items_dict.items():
        price = content.get('price','0.00')
        price = price_deformat(price)
        all_items_price += Decimal(price)
    total = str(Money(all_items_price + Decimal(price_deformat(commission)), currency="USD"))
    return total
def price_deformat(str_money):
    digit_list = [digit for digit in str_money if digit.isdigit() or digit == '.']
    str_price = ''.join(digit_list)
    return str_price
# i don't know why i made this a function in the first place
# Well now it's useful. Some users might lack profile pic
# i don't want to be overwhelmed by a ton of "try..except" and what-not... 
def get_profile_pic(user_objectid):
    try:
        any_user=User.Query.get(objectId=user_objectid)
        any_user_pic = any_user.profilePicture.url
    except:
        void = ''
        return void
    return any_user_pic

#get any user info, used for profileview
def get_user_info(cUser, request, user_id='',username=''):
    proDict={}
    try:
        proDict=request.session['userinfo']
        if user_id and proDict['id'] == user_id:
            return proDict
        if username and proDict['username'] == username:
            return proDict
    except KeyError:
        pass
    if user_id or username:
        screen_name=''
        pPicture=''
        anyName = '' if user_id else username
        anyMail = ''
        anyBio = ''
        anyRating = ''
        total_reviews = 0
        total_deliveries = total_reviews
        total_orders = 0
        is_verified = False
        is_cuser = False
        member_since=''
        reviews_dict={}
        try:
            anyUser = User.Query.get(objectId=user_id) if user_id else User.Query.get(username=username)
            user_id = anyUser.objectId
            pPicture = get_profile_pic(anyUser.objectId)
            anyName = anyUser.username
            anyMail = anyUser.email
            member_since_month = anyUser.createdAt.strftime("%B")[:3]
            member_since_year = anyUser.createdAt.year
            member_since = '{} {}'.format(member_since_month, member_since_year)
            anyReviews = review.Query.filter(reviewedUser=anyUser)
            k=0
            for any_review in anyReviews:
                k = k+1
                reviews_dict['review'+str(k)] = {'sender':{'name':any_review.reviewer.username,
                                                           'picture':get_profile_pic(any_review.reviewer.objectId)},
                                                 'rating':any_review.rating,'text':any_review.reviewText, 'pub_date':any_review.createdAt.date()}
            is_verified = anyUser.emailVerified
            try:
                anyRating = anyUser.userRating
                total_reviews = anyUser.totalReviews
                total_deliveries = anyUser.totalDeliveries
                total_orders = anyUser.totalOrders
            except AttributeError:
                pass    
            try:
                screen_name = anyUser.screenName
                
            except AttributeError:
                pass
            anyBio = anyUser.userBio
        except (AttributeError, QueryResourceDoesNotExist):
            pass
        if not anyRating:
            anyRating = 0
        
        if anyName == cUser.username :
            is_cuser = True
         
       
        # let's get everything in a dict object
        proDict={'id':user_id,'username':anyName, 'screen_name':screen_name,'is_verified':is_verified, 'is_cuser':is_cuser, 'email':anyMail, 'Bio':anyBio, 
                 'rating':anyRating, 'total_deliveries':total_deliveries, 'total_orders':total_orders, 'pPicture':pPicture,
                 'total_reviews':total_reviews, 'reviews':reviews_dict, 'member_since':member_since}
        if is_cuser:
            request.session['userinfo']=proDict
    return proDict

# A function to handle review and save them to Parse
def tripReview(cUser, review_form, key):
    ''' Takes every review and saves relevent information'''
    # 'request' variable used here is a ParseObject, not to confuse with a view request 
    dealer = ''
    try:
        
        reviewedRequest = request.Query.get(objectId=key)
        had_reviewed = review.Query.filter(reviewedRequest=reviewedRequest)
        if had_reviewed:
            return False
        traveler = reviewedRequest.tripId.traveler
        requester = reviewedRequest.Requester
        is_accepted = reviewedRequest.accepted
        if is_accepted:
            if traveler.username == cUser.username:
                dealer = requester
            elif requester.username == cUser.username:
                dealer = traveler
            else:
                return False 
    
       
        try:
            new_review_obj = review( reviewText=review_form.cleaned_data['text'], rating=review_form.cleaned_data['rating'])
            print reviewedRequest
            new_review_obj.reviewedRequest = reviewedRequest 
            new_review_obj.reviewer = cUser
            new_review_obj.reviewedUser = dealer
            
            new_review_obj.save()
            if requester.username == cUser.username:
                reviewedRequest.purchaserReview = new_review_obj
            else:
                reviewedRequest.travelerReview = new_review_obj
            reviewedRequest.save()   
            new_review_dic={'sender':{'name':new_review_obj.reviewer.username,
                                'picture':get_profile_pic(new_review_obj.reviewer.objectId)},'text':new_review_obj.reviewText,
                                'rating':new_review_obj.rating,'pubDate':new_review_obj.createdAt}  
            return new_review_dic
        except (AttributeError, QueryResourceDoesNotExist):
            pass
        
    except (AttributeError, QueryResourceDoesNotExist):
        pass
    
    return False

def ref_create(referralView, cUser, request):
    new_ref = referral(referrer=cUser)
    new_ref.save()
    #send a mail to the referred user with the "secret word" which will be used in referred signup, mandrill in play !
    personal_message = '{0} said: \n"'.format(cUser.Name) + referralView.cleaned_data['message'] + '"'
    link = request.build_absolute_uri(reverse('signup:register', args=['referral'])) + '?referral=' + new_ref.objectId
    
    send_mail = Function("email") #there is the same function in django, might play with that when porting
    result = send_mail(text='Your friend want to invite you in the amazing Airspress community.\n\n'+personal_message+'\n\nLink: '+link,
            subject="{0} invited you to join Airspress".format(cUser.username), from_email="no-reply@airspress.com",
            from_name="Airspress", email=referralView.cleaned_data['referred_email'], to_name='')
    
    alert = {'type':'warning', 'text':'There was an error attempting to send the invitation, try again later.'}
    try:
        if result["result"]=="email sent":
            alert = {'type':'success', 'text':'The invitation was succesfully sent !'}
    except KeyError:
        pass
    return alert


def notify(request, source, origin, target, target_id, email, text="", link="", activity_id=""):
    template_name = 'notifications'
    #  template variables

    if source =='accept_request':
        header = 'Request Accepted by ' + origin
        info = origin + " accepted you request."
        title="You made a request on " + origin + "'s trip earlier..."
        user = target
        action = 'Check Airdeal'
        link = request.build_absolute_uri(link)
        main = origin + " just accepted your request, you can now wrap up the details with the traveler and have your item delivered soon."
        subject = header + ':' + origin
        
        send_template(template_name=template_name,var_header=header, var_user = user, var_info=info, var_title=title,
                  var_main = main, var_action=action, subject=subject, email = email, 
                  from_name='Airspress',from_email = 'no-reply@airspress.com')
        try:
            push_alert = origin + ' accepted your request!'
            Push.alert({"alert": push_alert,"badge": "Increment"}, 
                   where={"appUser":{"__type":"Pointer","className":"_User","objectId":target_id}})
        except:
            pass
        target_user = User.Query.get(objectId = target_id)
        if getattr(target_user,'notifOutDeals',False):
            target_user.notifOutDeals.increment()
        else:
            target_user.notifOutDeals = 1
        target_user.save()
    elif source.startswith("message"):
        header = 'New Message from ' + origin
        info = origin + " sent you a message."
        title="This is " + origin + "'s message :"
        user = target
        action = 'Check your deal' if source.endswith('deal') else "Check your inbox"
        link = request.build_absolute_uri(link)
        main = text
        subject = header + ':' + origin
        
        # email alert
        send_template(template_name=template_name,var_header=header, var_user = user, var_info=info, var_title=title,
                  var_main = main, var_action=action, subject=subject, email = email, 
                  from_name='Airspress',from_email = 'no-reply@airspress.com')
        # Push to smartphone
        try:
            push_alert = origin + ' sent you a message!'
            Push.alert({"alert": push_alert,"badge": "Increment"}, 
                   where={"appUser":{"__type":"Pointer","className":"_User","objectId":target_id}})
        except:
            pass   
        # update User notifications counter
        target_user = User.Query.get(objectId = target_id)
        if not source.endswith('deal'):
            if getattr(target_user,'notifInbox',False):
                target_user.notifInbox.increment()
            else:
                target_user.notifInbox = 1
        else:
            this_deal = trequests.Query.get(objectId=activity_id)
            try:
                if this_deal.tripId.traveler.username == target_user.username:
                    if getattr(target_user,'notifInDeals',False):
                        target_user.notifInDeals.increment()
                    else:
                        target_user.notifInDeals = 1
                elif this_deal.Requester.username == target_user.username:
                    if getattr(target_user,'notifOutDeals',False):
                        target_user.notifOutDeals.increment()
                    else:
                        target_user.notifOutDeals = 1
            except AttributeError:
                pass        
        target_user.save()
    elif source=="new_request":
        header = 'Request Sent '
        info = origin + " sent you a request."
        title= origin + " made a request on your trip ..."
        user = target
        action = 'Check incoming requests'
        link = request.build_absolute_uri(link)
        main = origin + " just sent you a request, you can accept, check request details and carry on with the process."
        subject = header + ': ' + origin
        
        send_template(template_name=template_name,var_header=header, var_user = user, var_info=info, var_title=title,
                  var_main = main, var_action=action, subject=subject, email = email, 
                  from_name='Airspress',from_email = 'no-reply@airspress.com')
        try:
            push_alert = origin + ' sent you a request!'
            Push.alert({"alert": push_alert,"badge": "Increment"}, 
                   where={"appUser":{"__type":"Pointer","className":"_User","objectId":target_id}})
        except:
            pass
        target_user = User.Query.get(objectId = target_id)
        if getattr(target_user,'notifInDeals',False):
            target_user.notifInDeals.increment()
        else:
            target_user.notifInDeals = 1
        target_user.save()
    return True