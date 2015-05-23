"""
Forms for specific uses in non-member areas only

"""
from django import forms

class contact_form(forms.Form):
    name = forms.CharField()
    message = forms.CharField()
    subject = forms.CharField(required=False)
    reply_email = forms.EmailField()
    