from django.shortcuts import render
from tickets.forms import TicketForms, PersonForms

# Create your views here.

def index(request):
    form = TicketForms()
    person_form = PersonForms()
    context = {'form':form, 'person_form': person_form}
    return render(request, 'index.html', context)


def search_results(request):
    if request.method == 'POST':
        form = TicketForms(request.POST)
        person_form = PersonForms()
        if form.is_valid():
            context = {'form':form, 'person_form': person_form}
            return render(request, 'search_results.html', context)

        context = {'form':form}
        return render(request, 'index.html', context)
