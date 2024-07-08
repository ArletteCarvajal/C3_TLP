from django.urls import path, include
from .views import InicioView, Salir, registrar_produccion, registro_operador, inicio_sesion, consultar_produccion, modificar_produccion



urlpatterns = [
    
    path('', InicioView, name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', Salir, name='salir'),
    path('login/',inicio_sesion, name='inicio_sesion'),

    # path para registrar modificar y consultar producciones
    path('registrar_produccion/', registrar_produccion, name='registrar_p'),
    path('modificar_produccion/', modificar_produccion, name='modificar'),
    path('consultar_produccion/', consultar_produccion, name='consultar'),

    #path registro de un nuevo operador
    path('registrar_operador/', registro_operador, name='registrar_o'),
]
