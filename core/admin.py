from django.contrib import admin
from django.apps import AppConfig
from django.contrib.auth.models import Group
from .models import Operador, Plantas, Productos, Registro_Produccion, Supervisor, AnulacionHistorial

# Register your models here.

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        # Crear grupos si no existen
        Group.objects.get_or_create(name='supervisor')
        Group.objects.get_or_create(name='operador')


class PlantasAdmin(admin.ModelAdmin):
    list_display = ('nombre_planta', 'codigo_planta')


class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'codigo_producto', 'nombre_planta_')

    def nombre_planta_(self, obj):
        return obj.nombre_planta.nombre_planta

    nombre_planta_.short_description = 'Planta'


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('combustible', 'litros_produccion', 'fecha_produccion', 'turno', 'hora_registro', 'operador_nom', 'anulado')
    list_filter = ('anulado',)
    search_fields = ('codigo_combustible__codigo_producto', 'operador__user__username')
    actions = ['marcar_anulado', 'desmarcar_anulado']

    def combustible(self, obj):
        return obj.codigo_combustible.codigo_producto

    combustible.short_description = 'Combustible'

    def operador_nom(self, obj):
        return obj.operador.user.username

    operador_nom.short_description = 'Operador'

    def marcar_anulado(self, request, queryset):
        updated = queryset.update(anulado=True)
        self.message_user(request, f'Se marcaron como anulados {updated} registros.')

    def desmarcar_anulado(self, request, queryset):
        updated = queryset.update(anulado=False)
        self.message_user(request, f'Se desmarcaron como anulados {updated} registros.')

    marcar_anulado.short_description = 'Marcar como anulado'
    desmarcar_anulado.short_description = 'Desmarcar como anulado'


class AnulacionHistorialAdmin(admin.ModelAdmin):
    list_display = ('produccion', 'fecha_anulacion', 'anulado_por')
    search_fields = ('produccion__codigo_combustible__codigo_producto', 'anulado_por')

admin.site.register(Supervisor) # Para crear la tabla
admin.site.register(Operador) # Para crear la tabla
admin.site.register(Plantas, PlantasAdmin) # Para crear la tabla
admin.site.register(Productos, ProductosAdmin) # Para crear la tabla
admin.site.register(Registro_Produccion, RegistroAdmin) # Para crear la tabla
admin.site.register(AnulacionHistorial, AnulacionHistorialAdmin) # Para crear la tabla
