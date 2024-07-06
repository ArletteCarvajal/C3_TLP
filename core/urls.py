from django.urls import path, include
from rest.views import APPView



urlpatterns = [
    path("", APPView, name='APP'),

]
