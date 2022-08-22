from django import forms
from tempus_dominus.widgets import DatePicker


class TicketForms(forms.Form):
    origin = forms.CharField(label='Origem', max_length=100,)
    destiny = forms.CharField(label='Destino', max_length=100)
    departure_date = forms.DateField(label='Ida', widget=DatePicker())
    date_back = forms.DateField(label='Volta', widget=DatePicker())

