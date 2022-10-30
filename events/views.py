from django.shortcuts import render
from events.models import Speakers, Tracks, EventsGeneral, EventsParallel

# Create your views here.
def show_events_general(request):
    data = EventsGeneral.objects.all()
    data2 = EventsParallel.objects.all()

    context = {
        'list_item': data,
        'list_item2': data2,
    }

    return render(request, "eventsgeneral.html", context)