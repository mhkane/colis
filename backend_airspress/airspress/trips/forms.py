from django import forms
from airspress import settings
import datetime
class searchForm(forms.Form):
    depDate1 = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    depDate2 = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)
    cityDep = forms.CharField(required=False)
    cityArr = forms.CharField(required=False)

class addForm(forms.Form):
    # first trip
    depDate = forms.DateField( input_formats=settings.DATE_INPUT_FORMATS)
    arrivDate = forms.DateField( input_formats=settings.DATE_INPUT_FORMATS)
    weightGood = forms.IntegerField()
    # backtrip
    depDate2 = forms.DateField( input_formats=settings.DATE_INPUT_FORMATS, required=False)
    arrivDate2 = forms.DateField( input_formats=settings.DATE_INPUT_FORMATS, required=False)
    weightGood2 = forms.IntegerField(required=False)
    return_check = forms.BooleanField(required=False)
    # all
    cityDep = forms.CharField()
    cityArr = forms.CharField()
    # distance between places
    distance = forms.DecimalField(required=False)
    unit_price = forms.DecimalField()
    custom_price = forms.DecimalField(required=False)
    def clean(self):
        cleaned_data = super(addForm, self).clean()
        is_coming_back = cleaned_data.get('return_check')
        depart = cleaned_data.get('depDate2')
        arrival = cleaned_data.get('arrivDate2')
        weight = cleaned_data.get('weightGood2')
        if is_coming_back:
            msg = 'This field is required because you have roundtrip option selected'
            if not depart:
                self.add_error('depDate2', msg)
            if not arrival:
                self.add_error('arrivDate2', msg)
            if not weight:
                self.add_error('weightGood2', msg)
        return cleaned_data
        
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
    rating= forms.DecimalField()
    def clean_rating(self):
        data = self.cleaned_data['rating']
        return str(data)