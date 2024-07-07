# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registro_Produccion, AnulacionHistorial
from threading import local

_thread_locals = local()

def get_current_user():
    return getattr(_thread_locals, 'user', None)

class ThreadLocalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = request.user
        response = self.get_response(request)
        return response

@receiver(post_save, sender=Registro_Produccion)
def registro_anulacion(sender, instance, **kwargs):
    if instance.anulado and instance.pk:
        current_user = get_current_user()
        if current_user:
            AnulacionHistorial.objects.create(produccion=instance, anulado_por=current_user.username)
