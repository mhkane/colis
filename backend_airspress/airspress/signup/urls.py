from django.conf.urls import patterns, url

from signup import views
urlpatterns = patterns('',
    url(r'^$', views.home, name='index'),
    url(r'^login/(\w*)/', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^register/(\w*)/', views.signup, name='register'),
    )