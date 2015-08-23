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
	Planner.objects.all().delete()
	for flight in flights:
		Planner(title=flight.FlightCode, start=datetime.datetime.combine(flight.DepartureDate, flight.DepartureTime), end=datetime.datetime.combine(flight.DepartureDate,flight.ArrivalTime), description="Departs:" + flight.DepartureLocation + ", Arrives:" + flight.ArrivalLocation).save()
	
	planner = Planner.objects.all()
	planner_serialise = serializers.serialize('json', planner)		
	
	data = json.loads(planner_serialise)
	field_data = list()
	
	for d in data:
		del d['pk']
		del d['model']
		field_data.append(d['fields'])
		
		
	
	planner_json = json.dumps(field_data)

	return HttpResponse(planner_json)


