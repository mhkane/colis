from django.shortcuts import render
from signup.schemes import is_logged_in
from account.actions import get_profile_pic, send_mail
from airspress.forms import contact_form

def faq(request):
    cUser = is_logged_in(request)
    if cUser:
        return render(request, 'airspress/faq.html', {'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId)})
    return render(request, 'airspress/faq.html')
def about(request):
    cUser = is_logged_in(request)
    if cUser:
        return render(request, 'airspress/about.html', {'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId)})
    return render(request, 'airspress/about.html')
def contact(request):
    if request.method == 'POST' :
        new_contact = contact_form(request.POST)
        alert={'type':'danger', 'text':'Look at your entries, something is not right...'}
        if new_contact.is_valid():
            message = new_contact.cleaned_data['message']
            name = new_contact.cleaned_data['name']
            subject = new_contact.cleaned_data.get('subject','No subject')
            reply_email = new_contact.cleaned_data['reply_email']
            result = send_mail(text=message, subject=subject, from_email=reply_email, email='team@airspress.com', from_name=name, to_name='')
            alert = {'type':'warning', 'text':'There was an error attempting to send your message, try again later or catch us on <a href="https://twitter.com/airspress">Twitter</a>.'}
            try:
                if result["result"]=="email sent":
                    alert = {'type':'success', 'text':'Your message was succesfully sent ! We will contact you as soon as possible'}
                    result = send_mail(text='We received your message and we will answer you soon.\n\n Here is your message: \n\n'+message, subject='Contact:'+subject, from_email='no_reply@airspress.com' , email=reply_email, from_name='Airspress', to_name=name)
            except KeyError:
                pass
        return render(request,'signup/contact_ajx.html',{'contact_form':new_contact,'alert':alert})
        