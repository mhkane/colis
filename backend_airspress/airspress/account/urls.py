from django.conf.urls import patterns, url

from account import views, utils

urlpatterns = patterns('',

    url(r'^mytrips/add/$', views.addTrip, name='addtrip'),
    url(r'^mytrips/requested_trips/$', views.requestedTrips, name='myRequest'),
    url(ur'^edit/(?P<section>.*)/$', views.edit_profile, name='edit_profile'),
    url(ur'^referral/$', views.referral,name='referral'),
    url(ur'^usersRequest/$', views.otRequests, name='otRequest'),
    url(ur'^(?P<key>.*)/trips/$', views.myTrips, name='myTrip'),
    url(ur'^(?P<key>.*)/deals/$', views.deals, name='deals'),
    url(ur'^(?P<key>.*)/deals/review/$', views.reviewTrip, name='make_review'),
    url(ur'^(?P<key>.*)/$', views.profileView, name='profile'),
    url(r'^mix_manage/$',utils.mix_manage, name="parse_mix"),
    #url(r'^search', views.searchTrips, name='search'),
    
   )
