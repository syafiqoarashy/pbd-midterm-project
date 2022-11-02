from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#from authors.filters import AuthorsFilter
from .models import *
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_authors(request):
    authors_data = Authors.objects.all()
    authors_filter = AuthorsFilter(request.GET, queryset=authors_data)
    context = {
        'authors' : authors_data,
        'authors_filter':authors_filter
    }
    return render(request,"authors.html",context)

def show_details(request,id):
    authors_data = Authors.objects.filter(id=id)
    context = {
        'name' : authors_data
    }
    return render(request, "authdetails.html", context)

def show_json(request):
    authors_data = Authors.objects.all()
    authors_filter = AuthorsFilter(request.GET, queryset=authors_data)
    return HttpResponse(serializers.serialize("json", authors_filter.qs), content_type="application/json")