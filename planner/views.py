from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import requests, random, string, os,sys
from planit.settings import BASE_DIR
from django.core import serializers
from flights.models import Flight
from planner.models import Planner

def planner(request):
	return render(request, 'planner.html')

def planner_json(request):
	flights = Flight.objects.all()
	for flight in flights:
		planner = Planner(title=flight.FlightCode + " " + flight.DepartureLocation + " " + flight.ArrivalLocation, start=flight.DepartureDate, end=flight.DepartureDate)
		
		planner_json = serializers.serialize('json', planner)
		planner.save()
		return HttpResponse(planner_json)



