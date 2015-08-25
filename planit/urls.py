from django.conf.urls import patterns, include, url
from django.contrib import admin
from flights.views import flights_main
from django.conf import settings
from django.conf.urls.static import static
from flights.views import FlightListView, flights_refresh, flights_json
from planner.views import planner, planner_json, planner_create
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HttpResponseRedirect("/flights"), name='main'),
    url(r'^flights/$', flights_main, name='flights-detail' ),
    url(r'^flights/refresh', flights_refresh, name='refresh'),
    url(r'^flights/json', flights_json, name='flights_json'),
    url(r'^planner/$', planner, name='planner'),
    url(r'^planner/json', planner_json, name='planner_json'),
    url(r'^planner/create', planner_create, name='planner_create')
) 
