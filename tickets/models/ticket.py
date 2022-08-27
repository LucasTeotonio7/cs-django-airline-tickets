from django.db import models
from .travel_class import ClassTypes

class Ticket(models.Model):
    origin = models.CharField(verbose_name='Origem', max_length=100)
    destiny = models.CharField(verbose_name='Destino', max_length=100)
    departure_date = models.DateField(verbose_name='Data de ida')
    date_back = models.DateField(verbose_name='Data de volta')
    date_search = models.DateField(verbose_name='Data da pesquisa')
    informations = models.TextField(verbose_name='Informações', max_length=200, blank=True)
    travel_class = models.CharField(verbose_name='Classe', max_length=4,choices=ClassTypes.choices, default=0)
