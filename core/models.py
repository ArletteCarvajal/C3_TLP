from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Operador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Plantas(models.Model):    # modelo de plantas con sus nombres y contracción
    nombre_planta = models.CharField(max_length=100)
    codigo_planta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_planta


class Productos(models.Model): # modelo de productos, contracción o código y la planta de donde proviene
    nombre_producto = models.CharField(max_length=100)
    codigo_producto = models.CharField(max_length=3, primary_key=True)
    nombre_planta = models.ForeignKey(Plantas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_producto} - {self.codigo_producto} - {self.nombre_planta.nombre_planta}'


class Registro_Produccion(models.Model):
    codigo_combustible = models.ForeignKey(Productos, on_delete=models.CASCADE)
    litros_produccion = models.FloatField()
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length=6, choices=[('mañana', 'AM'), ('tarde', 'PM'), ('noche', 'MM')])
    hora_registro = models.TimeField()
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    anulado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.codigo_combustible.codigo_producto} - {self.litros_produccion} - {self.fecha_produccion} - {self.turno} - {self.hora_registro} - {self.operador.user.first_name}'


class AnulacionHistorial(models.Model):
    produccion = models.ForeignKey(Registro_Produccion, on_delete=models.CASCADE)
    fecha_anulacion = models.DateTimeField(auto_now_add=True)
    anulado_por = models.CharField(max_length=150, default=None)  # Almacena el nombre del usuario que anuló el registro

    def __str__(self):
        return f"{self.produccion} anulado por {self.anulado_por} el {self.fecha_anulacion}"


