from django.contrib import admin
from polls.models import Poll, Choice
from django.contrib.admin.options import TabularInline
# Register your models here.

class ChoiceInline(TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldset=[ (None, {'fields':['question']}),
              ('Date information', {'fields':['pub_date']}),
              ]
    inlines = [ChoiceInline]
    list_display = ['question','pub_date','was_published_recently']
    list_filter = ['pub_date']
admin.site.register(Poll, PollAdmin)
