from django import forms
from backend_parse import Institutions
from django.utils.translation import ugettext_lazy as _

all_institutions = Institutions.Query.all()
print all_institutions
AUTHORIZED_INSTITUTIONS = tuple((rank, auth_institution.name)  for rank, auth_institution in enumerate(all_institutions,1))

class regForm(forms.Form):
    login_name=forms.CharField()
    login_email=forms.EmailField()
    login_password = forms.CharField(min_length=8)
    login_password_conf = forms.CharField()
    tos_check = forms.BooleanField(required=False)
    def clean_login_password_conf(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("login_password")
        password2 = self.cleaned_data.get("login_password_conf")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2
class loginForm(forms.Form):
    login_username=forms.EmailField()
    login_password = forms.CharField()
# student register form, institution field added
class registerForm(regForm):
    login_institution = forms.ChoiceField(choices=AUTHORIZED_INSTITUTIONS)
# referred user register form
class ref_regForm(regForm):
    pass
#new password request 
class change_passForm(forms.Form):
    new_pass = forms.CharField(min_length=8, help_text=_("Your new password now... "))
    new_pass_conf = forms.CharField(help_text=_("Write again this all new password of yours and we're done"))
    def clean_new_pass_conf(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("new_pass")
        password2 = self.cleaned_data.get("new_pass_conf")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    
# for mail confirmation
class email_askForm(forms.Form):
    email = forms.EmailField()