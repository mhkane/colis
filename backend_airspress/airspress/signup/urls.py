from django.conf.urls import patterns, url

from signup import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='index'),
    url(r'^login/(\w*)/', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^register/(\w*)/', views.signup, name='register'),
    url(r'^mail_confirmation/', views.mail_confirmation, name='mailconf'),
    url(r'^forgot_password/$', views.pre_pass_reset, name='forgot_pass'),
    url(r'^reset_password/', views.pass_reset, name='reset_pass'),
    url(r'^email_verification/', views.email_verification, name="verification")
    )
