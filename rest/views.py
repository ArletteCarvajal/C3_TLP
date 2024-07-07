# rest/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Operador, Plantas, Productos, Registro_Produccion
from .serializers import OperadorSerializer, PlantasSerializer, ProductosSerializer, Registro_ProduccionsSerializer
from rest_framework import viewsets, status
from .utils import enviar_mensaje_slack
from core.forms import RegistroProduccionForm

def APPView(request):
    return render(request, 'core/inicio.html')

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

# @login_required
def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.operador = request.user
            registro.save()
            enviar_mensaje_slack(registro)
            return redirect('success_page')
    else:
        form = RegistroProduccionForm()
    return render(request, 'core/registrar_produccion.html', {'form': form})

# @login_required
def modificar_produccion(request, id):
    registro = Registro_Produccion.objects.get(id=id, operador=request.user)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'APP/modificar_produccion.html', {'form': form})

# @login_required
def consultar_produccion(request):
    registros = Registro_Produccion.objects.filter(operador=request.user)
    return render(request, 'APP/consultar_produccion.html', {'registros': registros})
