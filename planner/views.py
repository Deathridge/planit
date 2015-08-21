from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import requests, random, string, os,sys
from planit.settings import BASE_DIR
from django.core import serializers
from flights.models import Flight
from planner.models import Planner
import json

def planner(request):
	return render(request, 'planner.html')

def planner_json(request):
	flights = Flight.objects.all()
	for flight in flights:
		Planner(title=flight.FlightCode + " " + flight.DepartureLocation + " " + flight.ArrivalLocation, start=flight.DepartureDate, end=flight.DepartureDate).save()
	
	planner = Planner.objects.all()
	planner_json = serializers.serialize('json', planner)		
	
	data = json.loads(planner_json)

	for d in data:
		del d['pk']
		del d['model']
		d = d['fields'].data
	
	planner_json = json.dumps(data)

	return HttpResponse(planner_json)


