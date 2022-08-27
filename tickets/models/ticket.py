from django.db import models
from .travel_class import ClassTypes

class Ticket(models.Model):
    origin = models.CharField(max_length=100)
    destiny = models.CharField(max_length=100)
    departure_date = models.DateField()
    date_back = models.DateField()
    date_search = models.DateField()
    informations = models.TextField(max_length=200, blank=True)
    travel_class = models.CharField(max_length=4,choices=ClassTypes.choices, default=0)
