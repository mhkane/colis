from django import forms
from airspress import settings
import datetime
class searchForm(forms.Form):
    depDate1 = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    depDate2 = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    cityDep = forms.CharField(required=False)
    cityArr = forms.CharField(required=False)

class addForm(forms.Form):
    depDate = forms.DateField( input_formats=settings.DATE_INPUT_FORMATS)
    arrivDate = forms.DateField( input_formats=settings.DATE_INPUT_FORMATS)
    cityDep = forms.CharField()
    cityArr = forms.CharField()
    weightGood = forms.IntegerField()
    distance = forms.IntegerField(required=False)
class requestForm(forms.Form):
    item_name = forms.CharField()
    item_price = forms.DecimalField()
    item_quantity = forms.IntegerField()
    shop_name = forms.CharField()
    weightGood = forms.IntegerField()
    comments = forms.CharField()

class editproForm(forms.Form):
    paypalMail = forms.EmailField()
    userBio = forms.CharField()
    timeZone = forms.CharField()
    profilePic = forms.FileField(label='Select a picture', help_text ='max. 2mb' )
class reviewForm(forms.Form):
    text = forms.CharField(max_length=200)
    rating= forms.CharField()