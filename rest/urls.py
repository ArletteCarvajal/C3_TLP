from django.urls import path, include
from .views import APPView, OperadorViewSet, PlantasViewSet, ProductosViewSet, Registro_ProduccionViewSet, registrar_produccion, modificar_produccion, consultar_produccion
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'operador', OperadorViewSet)
router.register(r'plantas', PlantasViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'registros', Registro_ProduccionViewSet)

urlpatterns = [
    #path("", APPView, name='APP'),
    path("", include(router.urls)),
    path("registrar-produccion/", registrar_produccion, name='registrar_produccion'),
    path("modificar-produccion/<int:id>/", modificar_produccion, name='modificar_produccion'),
    path("consultar-produccion/", consultar_produccion, name='consultar_produccion'),
]
