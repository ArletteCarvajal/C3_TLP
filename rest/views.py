# rest/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Operador, Plantas, Productos, Registro_Produccion, Supervisor, RegistroModificacion
from .serializers import OperadorSerializer, PlantasSerializer, ProductosSerializer, Registro_ProduccionsSerializer, SupervisorSerializer
from rest_framework import viewsets, status
from .utils import enviar_mensaje_slack
from core.forms import RegistroProduccionForm, SupervisorForm, OperadorForm
from django.contrib import messages
from django.utils import timezone


def APPView(request):
    return render(request, 'core/inicio.html')

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

@login_required
def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            operador = Operador.objects.get(user=request.user)
            registro.operador = operador
            registro.turno = form.cleaned_data['turno']
            registro.save()
            enviar_mensaje_slack(registro)
            return redirect('inicio')
    else:
        form = RegistroProduccionForm()
    return render(request, 'core/registrar_produccion.html', {'form': form})


@login_required
def ver_registros(request):
    registros = Registro_Produccion.objects.all()
    return render(request, 'inicio.html', {'registros': registros})


@login_required
def editar_registro(request, pk):
    registro = get_object_or_404(Registro_Produccion, pk=pk)
    if registro.operador.user != request.user:
        messages.error(request, "No tienes permiso para editar este registro.")
        return redirect('inicio')
    
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            cambios = {}
            for field in form.changed_data:
                cambios[field] = getattr(registro, field)

            registro = form.save(commit=False)
            registro.modificado_por = request.user
            registro.modificado_en = timezone.now()
            registro.save()

            RegistroModificacion.objects.create(
                registro=registro,
                modificado_por=request.user,
                datos_antes=str(cambios)
            )

            messages.success(request, "Registro modificado correctamente.")
            return redirect('ver_registros')
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'editar_registro.html', {'form': form})




def registro_operador(request):
    if request.method == 'POST':
        form = OperadorForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar el grupo 'operador' al usuario
            group, created = Group.objects.get_or_create(name='operador')
            user.groups.add(group)
            # Crear el perfil de Operador
            Operador.objects.create(user=user)
            # Autenticar y loguear al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Reemplaza 'home' con tu URL de página principal
    else:
        form = OperadorForm()
    
    return render(request, 'core/registro_operador.html', {'form': form})

def registro_supervisor(request):
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar el grupo 'supervisor' al usuario
            group, created = Group.objects.get_or_create(name='supervisor')
            user.groups.add(group)
            # Crear el perfil de Supervisor
            Supervisor.objects.create(user=user)
            # Autenticar y loguear al usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Reemplaza 'home' con tu URL de página principal
    else:
        form = SupervisorForm()
    
    return render(request, 'core/registro_supervisor.html', {'form': form})

def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('inicio')  # Asegúrate de que 'inicio' es el nombre correcto de la ruta para tu página principal
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


