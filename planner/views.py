from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import requests, random, string, os,sys
from planit.settings import BASE_DIR
from django.core import serializers
from flights.models import Flight

def planner(request):
	return render(request, 'planner.html')

def events_json(request):
	flights = Flight.objects.all()
	json_flights = serializers.serialize('json', flights)

	return HttpResponse(json_flights)