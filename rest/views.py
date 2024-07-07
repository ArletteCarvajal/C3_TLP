# rest/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Operador, Plantas, Productos, Registro_Produccion, Supervisor
from .serializers import OperadorSerializer, PlantasSerializer, ProductosSerializer, Registro_ProduccionsSerializer, SupervisorSerializer
from rest_framework import viewsets, status
from .utils import enviar_mensaje_slack
from core.forms import RegistroProduccionForm, SupervisorForm, OperadorForm

def APPView(request):
    return render(request, 'core/inicio.html')

# CREACION DE CLASES PARA CRUD (Crear, Leer, Actualizar y Borrar) 

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer


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







#registro_usuario

def registro_supervisor(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            supervisor = Supervisor.objects.create(user=user)
            supervisor.save()
            # Asignar el usuario al grupo 'supervisor'
            group = Group.objects.get(name='supervisor')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Reemplaza 'home' con tu URL de página principal
    else:
        form = SupervisorForm()
    
    return render(request, 'core/registro_supervisor.html', {'form': form})

def registro_operador(request):
    if request.method == 'POST':
        form = OperadorForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            operador = Operador.objects.create(user=user)
            operador.save()
            # Asignar el usuario al grupo 'operador'
            group = Group.objects.get(name='operador')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Reemplaza 'home' con tu URL de página principal
    else:
        form = OperadorForm()
    
    return render(request, 'core/registro_operador.html', {'form': form})