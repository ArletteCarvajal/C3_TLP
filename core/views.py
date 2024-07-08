from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import Operador, Registro_Produccion, RegistroModificacion
from .forms import RegistroProduccionForm, OperadorForm
from rest.utils import enviar_mensaje_slack
from django.contrib import messages
from django.utils import timezone

def InicioView(request):
    return render(request, 'core/inicio.html')

#funcion para salir 
def Salir(request):
    logout(request)
    return redirect('inicio')

# CREACION DE CLASES PARA CRUD (Crear, Leer, Actualizar y Borrar) 

@login_required
def registros_del_usuario(request):
    registros = Registro_Produccion.objects.filter(operador=request.user)
    return render(request, 'core/registrar_produccion.html', {'registros': registros})
 

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


def modificar_produccion(request, pk):
    registro = get_object_or_404(Registro_Produccion, pk=pk)

    # Verificar si el usuario actual es el operador del registro
    if registro.operador != request.user:
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



#registro_usuacrio

def registro_operador(request):
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


def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            opcion = request.POST.get('opcion', None)
            
            if opcion == 'registrar':
                return redirect('registrar_produccion')  # Redireccionar a registrar producción
            elif opcion == 'modificar':
                return redirect('modificar_produccion')  # Redireccionar a modificar producción
            elif opcion == 'consultar':
                return redirect('consultar')  # Redireccionar a consultar producciones
            else:
                return render(request, 'inicio.html')  # Renderizar la página inicial si no hay opción válida
        
        else:
            # Manejar el caso de credenciales inválidas
            context = {'error_message': 'Credenciales inválidas'}
            return render(request, 'inicio.html', context)
    
    # Si no es un método POST, renderizar el formulario vacío o de inicio
    return render(request, 'registar_o.html')  # Asumo que 'registar_o.html' es el nombre correcto de tu template







"""
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

    """

"""@login_required
def modificar_produccion(request, id):
    registro = Registro_Produccion.objects.get(id=id, operador=request.user)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'core/modificar_produccion.html', {'form': form})"""