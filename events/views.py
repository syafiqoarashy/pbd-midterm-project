from django.shortcuts import render
from events.models import EventsGeneral, EventsParallel
import datetime

# Create your views here.
def show_events_general(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 22))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 22))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral.html", context)

def show_events_general23(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 23))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 23))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral23.html", context)

def show_events_general24(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 24))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 24))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral24.html", context)

def show_events_general25(request):
    data = EventsGeneral.objects.filter(date=datetime.date(2019, 7, 25))
    data2 = EventsParallel.objects.filter(date=datetime.date(2019, 7, 25))

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral25.html", context)