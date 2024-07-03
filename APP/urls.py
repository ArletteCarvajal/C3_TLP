#registración de los views a crear

from django.urls import path 
from .views import APPView
urlpatterns = [
    path ("", APPView, name='APP'),
    
]