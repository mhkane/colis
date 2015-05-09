'''
Relevant models (not Django db-backed models) to handle
user actions : put request on a travel, add a trip, make payments
and also edit profile information
'''
from signup.schemes import User
from parse_rest.datatypes import Object as ParseObject, Function
from email.mime.image import MIMEImage
from airspress.settings import FILE_UPLOAD_DIR
from django.core.urlresolvers import reverse
from parse_rest.query import QueryResourceDoesNotExist
from decimal import Decimal
from signup.backend_parse import reviews, referral

class request(ParseObject):
    pass

#Cloud function for mail sending
send_mail = Function("email")

# function to recover information for a given deal 
def getdeal(travelUser, reqUser, aRequest, aTrip):
    reqAccepted = {}
    try:
        #reqWeight = aRequest.weightRequested
        #priceDeal = aRequest.priceUsd
        pub_date = aRequest.createdAt
        departDate = aTrip.departureDate.date()
        arriDate = aTrip.arrivalDate.date()
        destLocation = aTrip.toLocation
        oriLocation = aTrip.fromLocation
        
    except AttributeError:
        pass
    reqUser_pic = ''
    traveler_pic=''
    try:
        reqUser_pic = reqUser.profilePicture.url
        traveler_pic = travelUser.profilePicture.url
        reqAccepted['ispayed']= aRequest.paymentStatus
        reqAccepted['isdeliv']= aRequest.deliveryStatus
    except AttributeError:
        pass
    reqAccepted = {'pubdate':pub_date, 'arrDate':arriDate,
             'depDate':departDate, 'cityDep':oriLocation, 
             'cityArr':destLocation,
             'traveler':{'username':travelUser.username,'picture':traveler_pic},
             'reqUser':{'username':reqUser.username,'picture':reqUser_pic}}
    # send notification
    print reqAccepted
    return reqAccepted
# TRASH we don't use this as we've configuring a cloud function to send the emails
def notif_mail(recipient_email, msg_a, msg_b):
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    # me == my email address
    # you == recipient's email address
    me = "team@airspress.com"
    you = recipient_email
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Notification"
    msg['From'] = me
    msg['To'] = you
    
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\n{0} {1}".format(msg_a, msg_b)
    fp = open(FILE_UPLOAD_DIR+'notif.html', 'rb')
    html = fp.read()
    fp.close()
    html.format(msg_a, msg_b)
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # This example assumes the image is in the current directory
    fp = open(FILE_UPLOAD_DIR+'im(1).jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)
    # Send the message via local SMTP server.
    s = smtplib.SMTP("mail.airspress.com", 26)
    #
    #s.connect('mail.airspress.com')
    s.ehlo()
    s.login('team@airspress.com', '@1rm@r$i@')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.close()
    return 0
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
        reviews_dict={}
        try:
            anyUser = User.Query.get(objectId=user_id) if user_id else User.Query.get(username=username)
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
         
        # crunch down the long usernames; this is the sick messy way
        # we can implement the slick Messi way afterwards ;-)
        for delim in ['.','@','_']:
            if delim in anyName:
                anyName = anyName.split(delim, 1)[0]
        # let's get everything in a dict object
        proDict={'id':user_id,'username':anyName, 'screen_name':screen_name,'is_verified':is_verified, 'is_cuser':is_cuser, 'email':anyMail, 'Bio':anyBio, 
                 'rating':anyRating, 'total_deliveries':total_deliveries, 'total_orders':total_orders, 'pPicture':pPicture,
                 'total_reviews':total_reviews, 'reviews':reviews_dict}
        if is_cuser:
            request.session['userinfo']=proDict
    return proDict

# A function to handle review and save them to Parse
def tripReview(cUser, review, key):
    ''' Takes every review and saves relevent information'''
    # 'request' variable used here is a ParseObject, not to confuse with a view request 
    from signup.backend_parse import reviews
    dealer = ''
    try:
        reviewedRequest = request.Query.get(objectId=key)
        traveler = reviewedRequest.traveler
        requester = reviewedRequest.requester
        is_accepted = reviewedRequest.accepted
    except (AttributeError, QueryResourceDoesNotExist):
        return False
    if is_accepted:
        if traveler==cUser:
            dealer = requester
        elif requester==cUser:
            dealer = traveler
        try:
            new_review = reviews(reviewedRequest=reviewedRequest, reviewer=cUser, reviewText=review.cleaned_data['text'], rating=Decimal(review.cleaned_data['rating']),
            reviewedUser= dealer)
            new_review.save()
            new_review={'sender':{'name':new_review.reviewer.username,
                                'picture':get_profile_pic(new_review.reviewer.objectId)},'text':new_review.reviewText,
                                'rating':new_review.rating,'pubDate':new_review.createdAt.date()}  
            return new_review
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