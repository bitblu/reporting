from django.conf.urls import patterns, include, url
from reporting import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'reporting.views.index', name='index'),
    url(r'^reporting/', include('reporting.urls', namespace="reporting")),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User Auth Url's
    url(r'^reporting/login/', 'bitblu.views.login'),
)
