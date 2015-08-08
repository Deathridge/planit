from django.db import models

# Create your models here.
class Flight(models.Model):	
	FlightCode = models.CharField(blank=False, null=False, primary_key=True, max_length=255)
	DepartureDate = models.DateField(blank=True,null=True)	
	DepartureTime = models.TimeField(blank=True, null=True)
	ArrivalTime = models.TimeField(blank=True, null=True)
	DepartureLocation = models.CharField(blank=True, null=True, max_length=255)
	ArrivalLocation = models.CharField(blank=True, null=True, max_length=255)
