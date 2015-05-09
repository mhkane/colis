from django import forms
from signup.forms import change_passForm

class referralForm(forms.Form):
    referred_email = forms.EmailField(help_text="Your friend email address")
    message = forms.CharField(required=False, 
                              help_text="""Hello, I've been using Airspress and i think it's very useful, fun 
                              and definitly worth trying.""")
#change password in account settings
class settings_form_password(change_passForm):
    current_pass = forms.CharField(help_text="This old password you want to change...")
#change general settings
class settings_form_general(forms.Form):
    screen_name = forms.CharField(max_length=10, required=False)
    time_zone = forms.CharField(required=False)
# profile picture setting
class settings_form_picture(forms.Form):
    profile_picture = forms.ImageField(help_text="2mb max.")