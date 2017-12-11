from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    header = loader.get_template('omiyage/layout/header.html')
    template = loader.get_template('omiyage/index.html')
    return HttpResponse(template.render())
