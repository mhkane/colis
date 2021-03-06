from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',

    url(r'^mytrips/add/$', views.addTrip, name='addtrip'),
    url(r'^mytrips/requested_trips/$', views.requestedTrips, name='myRequest'),
    url(ur'^edit/(?P<section>.*)/$', views.edit_profile, name='edit_profile'),
    url(ur'^inbox/$', views.inbox,name='inbox'),
    url(ur'^talk/(?P<key>.*)/$', views.instant_messaging,name='talk'),
    url(ur'^referral/$', views.referral,name='referral'),
    url(ur'^usersRequest/$', views.otRequests, name='otRequest'),
    url(ur'^(?P<key>.*)/trips/$', views.myTrips, name='myTrip'),
    url(ur'^(?P<key>.*)/deals/confirm_delivery/$', views.confirm_delivery, name='confirm_delivery'),
    url(ur'^(?P<key>.*)/deals/confirm_payment/$', views.confirm_payment, name='confirm_payment'),
    url(ur'^(?P<key>.*)/deals/review/$', views.reviewTrip, name='make_review'),
    url(ur'^(?P<key>.*)/deals/accept/$', views.accept_request, name='accept_request'),
    url(ur'^(?P<key>.*)/deals/$', views.deals, name='deals'),
    url(ur'^(?P<key>.*)/$', views.profileView, name='profile'),
    #url(r'^search', views.searchTrips, name='search'),
    
   )
