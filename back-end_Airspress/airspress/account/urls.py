from django.conf.urls import patterns, url

from account import views

urlpatterns = patterns('',
##    url(r'^$', views.IndexView.as_view(), name='index'),
##    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
##    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
##    url(r'^(?P<poll_id>\d+)/votes/$', views.votes, name='votes'),
    url(r'^mytrips/add/$', views.addTrip, name='addtrip'),
    url(r'^mytrips/requested_trips/$', views.requestedTrips, name='myRequest'),
    url(ur'^(?P<key>.*)/trips/$', views.myTrips, name='myTrip'),
    #url(r'^search', views.searchTrips, name='search'),
   )
