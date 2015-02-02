from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'airspress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls',namespace='polls')),
    url(r'^', include('signup.urls',namespace='signup')),
    url(r'^trips/', include('trips.urls',namespace='trips')),
    url(r'^account/', include('account.urls',namespace='account')),
    url(r'^payment/', include('asp_payment.urls',namespace='payment')),
    )
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
