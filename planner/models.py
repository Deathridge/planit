from django.db import models

# Create your models here.
class Planner(models.Model):	
	title = models.CharField(max_length=255)    
	start = models.DateTimeField(blank=True, null=True)
	end = models.DateTimeField(blank=True,null=True)
	description = models.CharField(max_length=255, null=True, blank=True)

