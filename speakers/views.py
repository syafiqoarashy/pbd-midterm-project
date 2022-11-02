from email.mime import application
from unicodedata import name
from urllib import request
from django.shortcuts import render
from speakers.models import Speakers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.template import loader
from django.core import serializers

class HomePageView(TemplateView):
    template_name = 'show_speakers.html'


class SearchResultsView(ListView):
    model = Speakers
    template_name = 'search_speakers.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Speakers.objects.filter(name__icontains=query)
        return object_list

def show_speakers(request):
    data_speakers = Speakers.objects.all()
    data_speakers_plenary = Speakers.objects.all().filter(type="plenary")
    data_speakers_keynote = Speakers.objects.all().filter(type="keynote")
    data_speakers_invited = Speakers.objects.all().filter(type="invited")
    
    context = {
    'list_speakers': data_speakers,
    'list_speakers_plenary': data_speakers_plenary,
    'list_speakers_keynote': data_speakers_keynote,
    'list_speakers_invited': data_speakers_invited
    }
    return render(request, 'show_speakers.html', context)
'''
def search_speakers(request):
    if request.method == 'POST':
        s_name = request.POST.get("name")
        s = Speakers.objects.all().filter(name=s_name)
        return HttpResponseRedirect(reverse("speakers:show_speakers"))
    context = {}
    return render(request, 'search_speakers.html', context)
'''

def show_speakers_info(request, id): # detailed info of speaker
    data_speakers = Speakers.objects.filter(pk=id)
    template = loader.get_template('show_speakers_info.html')
    #s_id = Speakers.objects.all().get(speakersId)
    context = {
        'speakers_info': data_speakers
    }
    #return HttpResponse(template.render(context, request), content_type="application/show_speakers_info/{}".format(id))
    return render(request, 'show_speakers_info.html', context)

def show_json(request):
    data = Speakers.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")