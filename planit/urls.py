from django.conf.urls import patterns, include, url
from django.contrib import admin
from flights.views import flights_main
from django.conf import settings
from django.conf.urls.static import static
from flights.views import FlightListView, flights_refresh
from planner.views import planner

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', flights_main, name='main'),
    url(r'^flights/$', flights_main, name='flights-detail' ),
    url(r'^flights/r', flights_refresh, name='refresh'),
    url(r'^planner/$', planner, name='planner'),
) 
