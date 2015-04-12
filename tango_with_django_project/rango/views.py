from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! <br> <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("About says: Hello world! <br> <a href='/rango'>Rango</a>")