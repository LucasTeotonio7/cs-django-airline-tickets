from django.shortcuts import render
from tickets.forms import TicketForms

# Create your views here.

def index(request):
    form = TicketForms()
    context = {'form':form}
    return render(request, 'index.html', context)
