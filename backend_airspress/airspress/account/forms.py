from django import forms

class referralForm(forms.Form):
    referred_mail = forms.EmailField()
    secret_word = forms.CharField(min_length=4)
