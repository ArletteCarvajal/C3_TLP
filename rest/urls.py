from django.urls import path, include
from .views import APPView, OperadorViewSet, PlantasViewSet, ProductosViewSet, Registro_ProduccionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'operador', OperadorViewSet)
router.register(r'plantas', PlantasViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'registros', Registro_ProduccionViewSet)

urlpatterns = [
    path("", APPView, name='inicio'),
    path("", include(router.urls)),
    
]
