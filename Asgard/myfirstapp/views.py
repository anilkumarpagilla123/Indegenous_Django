from django.shortcuts import render
from django.http import HttpResponse
from .models import Simple
from django.template import loader

def say_hello(request):
    mydata = Simple.objects.all().values()
    template = loader.get_template('asgard.html')
    context = {
    'data': mydata
    }
    return HttpResponse(template.render(context, request))