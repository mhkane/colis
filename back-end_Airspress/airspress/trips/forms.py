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
class requestForm(forms.Form):
    weightGood = forms.IntegerField()
    comments = forms.CharField()