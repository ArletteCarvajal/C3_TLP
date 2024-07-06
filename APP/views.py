# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Operador, Plantas, Productos, Registro_Produccion
from .serializers import OperadorSerializer, PlantasSerializer, ProductosSerializer, Registro_ProduccionsSerializer
from rest_framework import viewsets 
def APPView(request):
    return render (request, 'APP/inicio.html') #retornamos en los aprentesis, la requisito que es el parametro, la app que es donde está y el nombre del template

# CREACION DE CLASES PARA CRUD acrónimo de "Crear, Leer, Actualizar y Borrar" 

class OperadorViewSet (viewsets.ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer

class PlantasViewSet (viewsets.ModelViewSet):
    queryset = Plantas.objects.all()
    serializer_class = PlantasSerializer

class ProductosViewSet (viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class Registro_ProduccionViewSet (viewsets.ModelViewSet):
    queryset = Registro_Produccion.objects.all()
    serializer_class = Registro_ProduccionsSerializer
