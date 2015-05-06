from django import forms
from signup.forms import change_passForm

class referralForm(forms.Form):
    referred_mail = forms.EmailField()
    secret_word = forms.CharField(min_length=4)
#change password in account settings
class settings_form_password(change_passForm):
    current_pass = forms.CharField()
#change general settings
class settings_form_general(forms.Form):
    screen_name = forms.CharField(max_length=10, required=False)
    time_zone = forms.CharField(required=False)
# profile picture setting
class settings_form_picture(forms.Form):
    profile_picture = forms.ImageField(help_text="2mb max.")