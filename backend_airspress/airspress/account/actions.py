'''
Relevant models (not Django db-backed models) to handle
user actions : put request on a travel, add a trip, make payments
and also edit profile information
'''
from signup.schemes import User
from parse_rest.datatypes import Object as ParseObject
from email.mime.image import MIMEImage
from airspress.settings import FILE_UPLOAD_DIR
class request(ParseObject):
    pass
class acceptedRequest(ParseObject):
    pass
# we have a referral class which is useful for retaining information between the referred and the referrer
# And there is the secret-word the referred enter at signup, best way to store that
class referral(ParseObject):
    pass
def getdeal(travelUser, aRequest, aTrip):
    reqAccepted = {}
    try:
        reqWeight = aRequest.weightRequested
        reqUser = aRequest.Requester
        travelName = travelUser.username
        #priceDeal = aRequest.priceUsd
        pub_date = aRequest.createdAt
        departDate = aTrip.departureDate.date()
        destLocation = aTrip.toLocation
        oriLocation = aTrip.fromLocation
        reqAccepted = {'pubdate':pub_date, 
             'depDate':departDate, 'cityDep':destLocation, 
             'cityArr':oriLocation,'requestWeight':reqWeight, 
             'traveler':travelName, 'travelerEmail':'', 'reqUser':reqUser.username, 'reqEmail':''}
        reqEmail=reqUser.email
        travelEmail = travelUser.email
        reqAccepted['travelerEmail']=travelEmail
        reqAccepted['reqEmail'] = reqEmail
    except AttributeError:
        pass
    reqAccepted['ispayed']= aRequest.paymentStatus or False
    reqAccepted['isdeliv']= aRequest.deliveryStatus or False
    
    # send notification
    
    return reqAccepted
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
def get_profile_pic(user_objectid):
    any_user=User.Query.get(objectId=user_objectid)
    any_user_pic = any_user.profilePicture.url
    return any_user_pic
def ref_create(referralView, cUser):
    new_ref = referral(referrer=cUser,secret=referralView.cleaned_data['secret_word'])
    new_ref.save()
    #send a mail to the referred user with the "secret word", mandrill in play !
    from parse_rest.datatypes import Function
    send_mail = Function("email") #there is the same function in django, might play with that when porting
    result = send_mail(text='Your friend want to invite you in the amazing Airspress community',
            subject="{0} invited you to join Airspress".format(cUser.username), from_email="no-reply@airspress.com",
            from_name="Airspress", email=referralView.cleaned_data['referred_mail'], to_name='')
    alert = {'type':'warning', 'text':'There was an error attempting to send the invitation, try again later.'}
    try:
        if result["result"]=="email sent":
            alert = {'type':'success', 'text':'The invitation was succesfully sent !'}
    except KeyError:
        pass
    return alert