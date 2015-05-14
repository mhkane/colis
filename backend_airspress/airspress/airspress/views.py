from django.shortcuts import render
from signup.schemes import is_logged_in
from account.actions import get_profile_pic

def faq(request):
    cUser = is_logged_in(request)
    if cUser:
        return render(request, 'airspress/faq.html', {'greetings':cUser.username,'myPicture':get_profile_pic(cUser.objectId)})
    return render(request, 'airspress/faq.html')