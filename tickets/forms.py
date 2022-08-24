from django import forms

class TicketForms(forms.Form):
    origin = forms.CharField(label='Origem', max_length=100)
    destiny = forms.CharField(label='Destino', max_length=100)
