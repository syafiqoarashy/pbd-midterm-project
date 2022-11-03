from unicodedata import name
from django.shortcuts import render
from speakers.models import Speakers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView

class HomePageView(TemplateView):
    template_name = 'show_speakers.html'

class search_speakers(ListView):
    model = Speakers
    template_name = 'search_speakers.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Speakers.objects.filter(name__icontains=query)
        return object_list

def show_speakers(request):
    data_speakers_plenary = Speakers.objects.all().filter(type="plenary")
    data_speakers_keynote = Speakers.objects.all().filter(type="keynote")
    data_speakers_invited = Speakers.objects.all().filter(type="invited")
    
    context = {
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

def show_speakers_info(request):
    if request.method == 'POST':
        s_name = request.POST.get("name")
    data_speakers = Speakers.objects.all().filter(name=s_name)
    context = {
        'speakers_info': data_speakers
    }
    return render(request, 'show_speakers_info.html', context)