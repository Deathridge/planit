from django.db import models

# Create your models here.
class Planner(models.Model):	
	title = models.CharField(max_length=255)    
    start = models.DateTimeField()
    end = models.DateTimeField()