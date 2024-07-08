from django.urls import path, include
from .views import  Salir, registrar_produccion, registro_operador, inicio_sesion, modificar_produccion, InicioView, registros_del_usuario



urlpatterns = [
    path('',InicioView, name= 'inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', Salir, name='salir'),
    path('login/',inicio_sesion, name='inicio_sesion'),

    # path para registrar modificar y consultar producciones
    path('registrar_produccion/',registrar_produccion, name='registrar_produccion'),
    path('modificar/<int:pk>/', modificar_produccion, name='modificar_produccion'),
    path ('registros_del_usuario/',registros_del_usuario, name='registros_del_usuario'),
    #path registro de un nuevo operador
    path('registrar_operador/', registro_operador, name='registrar_o'),
]
