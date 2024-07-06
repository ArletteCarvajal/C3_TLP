from django.shortcuts import render
from django.http import HttpResponse
from .models import Operador, Plantas, Productos, Registro_Produccion
from .serializers import OperadorSerializer, PlantasSerializer, ProductosSerializer, Registro_ProduccionsSerializer
from rest_framework import viewsets, status
from .utils import enviar_mensaje_slack  # Importar la función de utilidades

def APPView(request):
    return render(request, 'APP/inicio.html')

# CREACION DE CLASES PARA CRUD (Crear, Leer, Actualizar y Borrar) 

class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer

class PlantasViewSet(viewsets.ModelViewSet):
    queryset = Plantas.objects.all()
    serializer_class = PlantasSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class Registro_ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Registro_Produccion.objects.all()
    serializer_class = Registro_ProduccionsSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            registro = Registro_Produccion.objects.get(pk=response.data['id'])
            enviar_mensaje_slack(registro)
        return response
