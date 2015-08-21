from django.contrib import admin
from flights.models import Flight
from planner.models import Planner
# Register your models here.
admin.site.register(Flight)
admin.site.register(Planner)