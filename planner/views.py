from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import requests, random, string, os,sys
from planit.settings import BASE_DIR
from django.core import serializers
from flights.models import Flight
from planner.models import Planner
import datetime
import simplejson, json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def planner(request):
	return HttpResponse(request, 'planner.html')

def planner_json(request):
	flights = Flight.objects.all()
	Planner.objects.filter(protect=False).delete()
	for flight in flights:
		Planner(title=flight.FlightCode, start=datetime.datetime.combine(flight.DepartureDate, flight.DepartureTime), end=datetime.datetime.combine(flight.DepartureDate,flight.ArrivalTime), description="Departs: " + flight.DepartureLocation + "'\n' Arrives: " + flight.ArrivalLocation).save()
	
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

@csrf_exempt
def planner_create(request):
	print request.body
	if request.method == "POST":
		received_data = simplejson.loads(request.body)

		Planner(title=received_data['title'], start=received_data['start'], end=received_data['end'], description=received_data['description'], protect=True).save()
		return HttpResponse(received_data)
