from django.conf.urls import patterns, url

from account import views, utils

urlpatterns = patterns('',
##    url(r'^$', views.IndexView.as_view(), name='index'),
##    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
##    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
##    url(r'^(?P<poll_id>\d+)/votes/$', views.votes, name='votes'),
    url(r'^mytrips/add/$', views.addTrip, name='addtrip'),
    url(r'^mytrips/requested_trips/$', views.requestedTrips, name='myRequest'),
    url(ur'^(?P<key>.*)/trips/$', views.myTrips, name='myTrip'),
    url(ur'^(?P<key>.*)/deals/$', views.deals, name='deals'),
    url(ur'^usersRequest/$', views.otRequests, name='otRequest'),
    url(ur'^(?P<key>.*)/$', views.profileView, name='profile'),
    url(r'^mix_manage/$',utils.mix_manage, name="parse_mix"),
    #url(r'^search', views.searchTrips, name='search'),
    
   )
