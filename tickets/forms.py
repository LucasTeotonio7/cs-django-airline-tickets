from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from tickets.class_types import class_types


class TicketForms(forms.Form):
    origin = forms.CharField(label='Origem', max_length=100,)
    destiny = forms.CharField(label='Destino', max_length=100)
    departure_date = forms.DateField(label='Ida', widget=DatePicker())
    date_back = forms.DateField(label='Volta', widget=DatePicker())
    date_search = forms.DateField(label='Data da Pesquisa', widget=DatePicker(), disabled=True, initial=datetime.today())
    travel_class = forms.ChoiceField(label='Classe', choices=class_types)
    informations = forms.CharField(
        label='Informações extras',
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='email', max_length=150)

