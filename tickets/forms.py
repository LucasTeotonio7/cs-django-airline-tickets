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

    def clean_origin(self):
        origin = self.cleaned_data.get("origin")

        if any(char.isdigit() for char in origin):
            raise forms.ValidationError('Origem inválida: o campo não pode ter caracteres númericos')

        return origin

    def clean_destiny(self):
        destiny = self.cleaned_data.get("destiny")

        if any(char.isdigit() for char in destiny):
            raise forms.ValidationError('Destino inválido: o campo não pode ter caracteres númericos')

        return destiny


