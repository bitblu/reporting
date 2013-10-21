from django.conf.urls import patterns, include, url
from reporting import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'reporting.views.base', name='base'),

    # User Auth Urls
    url(r'^$', 'reporting.views.login'),
    url(r'^$', 'reporting.views.loggedin'),



)
