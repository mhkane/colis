from django.conf.urls import patterns, url

from trips import views

urlpatterns = patterns('',
##    url(r'^$', views.IndexView.as_view(), name='index'),
##    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
##    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
##    url(r'^(?P<poll_id>\d+)/votes/$', views.votes, name='votes'),
    url(r'^$', views.activeTrips, name='index'),
    url(r'^search', views.searchTrips, name='search'),
   )
