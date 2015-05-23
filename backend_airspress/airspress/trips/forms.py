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
    arrivDate = forms.DateField( input_formats=settings.DATE_INPUT_FORMATS, required=False)
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
        weight = cleaned_data.get('weightGood2')
        if is_coming_back:
            msg = 'This field is required because you have roundtrip option selected'
            if not depart:
                self._errors['depDate2'] =  self.error_class([msg])
            if not weight:
                self._errors['weightGood2'] = self.error_class([msg])
        return cleaned_data
        
class requestForm(forms.Form):
    item_name = forms.CharField()
    item_price = forms.DecimalField()
    item_quantity = forms.IntegerField()
    shop_name = forms.CharField()
    weightGood = forms.IntegerField()
    comments = forms.CharField()
    dimensions_1 = forms.IntegerField(required=False)
    dimensions_2 = forms.IntegerField(required=False)
    dimensions_3 = forms.IntegerField(required=False)
    request1 = forms.BooleanField(required=False)
    request2 = forms.BooleanField(required=False)
    
    def clean(self):
        cleaned_data = super(requestForm, self).clean()
        price = cleaned_data.get('item_price')
        name = cleaned_data.get('item_name')
        quantity = cleaned_data.get('quantity')
        shop = cleaned_data.get('shop_name')
        weight = cleaned_data.get('weightGood')
        comment = cleaned_data.get('comments')
        msg = 'Error'
        if not (weight or name or quantity):
            self._errors['request1'] = self.error_class([msg])
        elif not(price or comment or shop):
            self._errors['request2'] = self.error_class([msg]) 
        return cleaned_data
    
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