from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from rest.utils import enviar_mensaje_slack

class Operador(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nombre

class Plantas(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=3, primary_key=True)
    planta = models.ForeignKey(Plantas, on_delete=models.CASCADE)

class Registro_Produccion(models.Model):
    codigo_combustible = models.CharField(max_length=10)
    litros_producidos = models.IntegerField(default=0)
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length=2, choices=(('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')))
    hora_registro = models.TimeField()
    operador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros_operador')
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros_creados', default=None)
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registros_modificados', null=True, blank=True)
    fecha_modificacion = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            self.fecha_modificacion = timezone.now()
            self.modificado_por = self.operador
        else:
            self.creado_por = self.operador
            enviar_mensaje_slack(self)
        super(Registro_Produccion, self).save(*args, **kwargs)
