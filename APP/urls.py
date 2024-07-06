#registración de los views a crear

from django.urls import path, include 
from .views import APPView, OperadorViewSet, PlantasViewSet, ProductosViewSet, Registro_ProduccionViewSet
from rest_framework.routers import DefaultRouter  #para ordenar las urls de la API y mapaearlas a vistas especificas


router = DefaultRouter() # establece automáticamente las rutas para el CRUD

router.register(r'operador', OperadorViewSet)
router.register(r'plantas', PlantasViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'resgistros', Registro_ProduccionViewSet)

urlpatterns = [
    path ("", APPView, name='APP'),
    path ("", include(router.urls)),
]