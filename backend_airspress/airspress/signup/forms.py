from django import forms

class registerForm(forms.Form):
    login_email=forms.EmailField()
    login_password = forms.CharField(min_length=8)
    login_institution = forms.CharField()
class loginForm(forms.Form):
    login_email=forms.EmailField()
    login_password = forms.CharField()