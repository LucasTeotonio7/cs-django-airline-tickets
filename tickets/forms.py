from django import forms

from tempus_dominus.widgets import DatePicker
from datetime import datetime

from tickets.class_types import class_types
from tickets.validation import *


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

    def clean(self):
        origin = self.cleaned_data.get("origin")
        destiny = self.cleaned_data.get("destiny")
        departure_date = self.cleaned_data.get("departure_date")
        date_back = self.cleaned_data.get("date_back")
        errors_list = {}
        field_has_number(origin, 'origin', errors_list)
        field_has_number(destiny, 'destiny', errors_list)
        equals_origin_destiny(origin, destiny, errors_list)
        departure_is_greater_than_back(departure_date, date_back, errors_list)

        if errors_list is not None:
            for error in errors_list:
                error_msg = errors_list[error]
                self.add_error(error, error_msg)

        return self.changed_data


