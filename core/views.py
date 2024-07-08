from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import Operador, Registro_Produccion
from .forms import RegistroProduccionForm, OperadorForm


def InicioView(request):
    return render(request, 'core/inicio.html')

#funcion para salir 
def Salir(request):
    logout(request)
    return redirect('inicio')



# CREACION DE CLASES PARA CRUD (Crear, Leer, Actualizar y Borrar) 

@login_required
def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            form.instance.Operador = request.user.Operador
            registro.save()
            return redirect('inicio')  # Redirige a la vista deseada después de guardar
    else:
        form = RegistroProduccionForm()
    return render(request, 'core/registrar_produccion.html', {'form': form})

@login_required
def modificar_produccion(request, id):
    registro = Registro_Produccion.objects.get(id=id, operador=request.user)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'core/modificar_produccion.html', {'form': form})

@login_required
def consultar_produccion(request):
    registros = Registro_Produccion.objects.filter(operador=request.user)
    return render(request, 'core/consultar_produccion.html', {'registros': registros})


#registro_usuario

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
                return redirect('registrar_p')  # Redireccionar a registrar producción
            elif opcion == 'modificar':
                return redirect('modificar')  # Redireccionar a modificar producción
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