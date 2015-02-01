from django.conf.urls import patterns, url

from asp_payment import views

urlpatterns = patterns('',
    url(ur'^(?P<rqkey>.*)/paypal/create/$',views.paypal_create, name='paypal_create'),
    url(ur'^(?P<rqkey>.*)/paypal/execute/$',views.paypal_execute, name='paypal_execute'),
    url(ur'^(?P<rqkey>.*)/payment_success/$',views.payment_success, name= 'paysuccess'),
    url(ur'^(?P<rqkey>.*)/payment_error/$',views.payment_invalid, name='payinvalid'),    
)