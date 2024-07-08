from django.urls import path, include
from .views import APPView, OperadorViewSet, PlantasViewSet, ProductosViewSet, Registro_ProduccionViewSet, registrar_produccion, editar_registro, ver_registros
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'operador', OperadorViewSet)
router.register(r'plantas', PlantasViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'registros', Registro_ProduccionViewSet)

urlpatterns = [
    path("", APPView, name='inicio'),
    path("", include(router.urls)),
    path("registrar-produccion/", registrar_produccion, name='registrar_produccion'),
    path('editar_registro/<int:pk>/', editar_registro, name='editar_registro'),
    path("ver_registros/", ver_registros, name='consultar_produccion'),
]
