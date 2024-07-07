from django.contrib import admin
from django.contrib import admin
from .models import Operador, Plantas, Productos, Registro_Produccion, Supervisor
from django.apps import AppConfig
from django.contrib.auth.models import Group

# Register your models here.

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        # Crear grupos si no existen
        Group.objects.get_or_create(name='supervisor')
        Group.objects.get_or_create(name='operador')


#clase para que en las tablas de la BBDD se vean los nombres, codigo y planta  y no como object
class PlantasAdmin(admin.ModelAdmin):
    list_display = ('nombre_planta', 'codigo_planta')


#clase para que en las tablas de la BBDD se vean los nombres, codigo y planta  y no como object
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'codigo_producto', 'nombre_planta_')

    def nombre_planta_(self, obj):
        return obj.nombre_planta.nombre_planta

    nombre_planta_.short_description = 'Planta'


#clase para que en las tablas de la BBDD se vean los nombres, codigo y planta  y no como object
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('combustible', 'litros_produccion', 'fecha_produccion', 'turno', 'hora_registro', 'operador_nom')
    
    def combustible (self, obj):
        return obj.codigo_combustible.codigo_producto

    combustible.short_description = 'Combustible'

    def operador_nom(self, obj):
        return obj.operador.nombre_operador

    operador_nom.short_description = 'Operador'


admin.site.register(Supervisor) #para crear la tabla
admin.site.register(Operador) #para crear la tabla
admin.site.register(Plantas, PlantasAdmin) #para crear la tabla
admin.site.register(Productos, ProductosAdmin) #para crear la tabla
admin.site.register(Registro_Produccion, RegistroAdmin) #para crear la tabla