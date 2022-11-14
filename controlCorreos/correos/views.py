from django.shortcuts import render
from django.http import HttpResponse
from .models import Residencia
from .models import Correspondencia

# Create your views here.

def home(request):

    return render(request,'correos/home.html')

def residencias(request):
    residencias = Residencia.objects.all()

    return render(request,'correos/residencias.html',{'residencias':residencias})

def correspondencias(request):
    correspondencias = Correspondencia.objects.all()

    return render(request,'correos/correspondencias.html',{'correspondencias':correspondencias})