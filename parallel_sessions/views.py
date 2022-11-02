from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Tracks
from django.core import serializers
from django.http import HttpResponse

# Create your views here.


def category(request) :
    tracks = Tracks.objects.all()
    context = {
        'tracks': tracks,
    }
    return render(request, 'category.html', context)

def show_json_category(request):
    data = Tracks.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

