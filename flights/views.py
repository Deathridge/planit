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

def flights_main(request):
	form = SubmitFlight()

	if request.method == "POST":
		form = SubmitFlight(request.POST)

		if form.is_valid():

			FlightCode = form.cleaned_data['FlightCode']
			DepartureDate = form.cleaned_data['DepartureDate']
			data = scrapeflight(str(FlightCode), str(DepartureDate))
			DepartureTime = data[4]
			ArrivalTime = data[5]
			DepartureLocation = data[2]
			ArrivalLocation = data[3]
			

			flight = Flight(FlightCode=FlightCode,DepartureDate=DepartureDate,DepartureTime=DepartureTime,ArrivalTime=ArrivalTime, DepartureLocation=DepartureLocation,ArrivalLocation=ArrivalLocation)
			flight.save()

	else:

		form = SubmitFlight()

	return render(request, 'flight.html', {'form': form})

class FlightListView(ListView):

	model = Flight
	template_name = os.path.join(BASE_DIR, 'flights/templates/flight_list.html')
	
def flights_refresh(request):
	flights = Flight.objects.get()

	return HttpResponse(flights)