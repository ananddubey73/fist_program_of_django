from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):

    return HttpResponse('<h1><marquee>hi jampandu how are you</h1></marquee>')

def appname(request):
    return HttpResponse('<h1><marquee>Django is a framework application</h1></marquee>')
    
