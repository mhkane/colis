from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()


urlpatterns = patterns('', 
    url(r'session_security/', include('session_security.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('signup.urls',namespace='signup')),
    url(r'^trips/', include('trips.urls',namespace='trips')),
    url(r'^account/', include('account.urls',namespace='account')),
    url(r'^payment/', include('asp_payment.urls',namespace='payment')),
    url(r'^contact/',views.contact, name='contact'),
    )
urlpatterns += i18n_patterns('',
    # Examples:
    #url(r'^$', 'airspress.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('signup.urls',namespace='signup')),
    url(r'^trips/', include('trips.urls',namespace='trips')),
    url(r'^account/', include('account.urls',namespace='account')),
    url(r'^payment/', include('asp_payment.urls',namespace='payment')),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^faq/',views.faq, name='faq'),
    url(r'^about/',views.about, name='about'),
    url(r'^terms/',views.terms, name='terms'),
    )
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
