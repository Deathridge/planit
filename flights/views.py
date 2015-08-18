from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import requests, random, string, os,sys
from django.utils import timezone
from planit.settings import BASE_DIR
from django.views.generic.list import ListView
from .forms import SubmitFlight
from .models import Flight
from django.core.exceptions import ValidationError
from .query import scrapeflight
from django.contrib import messages

def flights_main(request):
	form = SubmitFlight()

	if request.method == "POST":
		form = SubmitFlight(request.POST)

		if form.is_valid():

			FlightCode = form.cleaned_data['FlightCode']
			DepartureDate = form.cleaned_data['DepartureDate']
			data = scrapeflight(str(FlightCode), str(DepartureDate))
			if (data[6] == 2):
				DepartureTime = data[4]
				ArrivalTime = data[5]
				DepartureLocation = data[2]
				ArrivalLocation = data[3]
			

				flight = Flight(FlightCode=FlightCode,DepartureDate=DepartureDate,DepartureTime=DepartureTime,ArrivalTime=ArrivalTime, DepartureLocation=DepartureLocation,ArrivalLocation=ArrivalLocation)
				flight.save()
			elif (data[6] == 0):
				messages.add_message(request, messages.ERROR, 'Invalid FlightCode')
			elif (data[6] == 1):
				messages.add_message(request, messages.ERROR, 'No flight data for provided date')

	else:
		
		form = SubmitFlight()
	
	flights = Flight.objects.all()
	return render(request, 'flight.html', {'form': form, 'object_list': flights})

class FlightListView(ListView):

	model = Flight
	template_name = os.path.join(BASE_DIR, 'flights/templates/flight_list.html')
	
def flights_refresh(request):
	flights = Flight.objects.all()

	return render(request, 'flight_table.html', {'object_list': flights})