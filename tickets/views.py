from django.shortcuts import render
from tickets.forms import TicketForms

# Create your views here.

def index(request):
    form = TicketForms()
    context = {'form':form}
    return render(request, 'index.html', context)


def search_results(request):
    if request.method == 'POST':
        form = TicketForms(request.POST)
        if form.is_valid():
            context = {'form':form}
            return render(request, 'search_results.html', context)

        context = {'form':form}
        return render(request, 'index.html', context)
