# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def APPView(request):
    return render (request, 'APP/inicio.html') #retornamos en los aprentesis, la requisito que es el parametro, la app que es donde está y el nombre del template

