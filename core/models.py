from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Operador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Plantas(models.Model):
    nombre_planta = models.CharField(max_length=100)
    codigo_planta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_planta

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=100)
    codigo_producto = models.CharField(max_length=3, primary_key=True)
    nombre_planta = models.ForeignKey(Plantas, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_producto} - {self.codigo_producto} - {self.nombre_planta.nombre_planta}'

class Registro_Produccion(models.Model):
    TURNO_CHOICES = [
        ('AM', 'AM'),
        ('PM', 'PM'),
        ('MM', 'MM')
    ]

    codigo_combustible = models.ForeignKey(Productos, on_delete=models.CASCADE)
    litros_produccion = models.FloatField()
    fecha_produccion = models.DateField(auto_now_add=True)
    turno = models.CharField(max_length=2, choices=TURNO_CHOICES)
    hora_registro = models.TimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    anulado = models.BooleanField(default=False)
    modificado_por = models.ForeignKey(User, related_name='modificados', null=True, blank=True, on_delete=models.SET_NULL)
    modificado_en = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.codigo_combustible.codigo_producto} - {self.litros_produccion} - {self.fecha_produccion} - {self.turno} - {self.hora_registro} - {self.operador.user.first_name}'



class AnulacionHistorial(models.Model):
    produccion = models.ForeignKey(Registro_Produccion, on_delete=models.CASCADE)
    fecha_anulacion = models.DateTimeField(auto_now_add=True)
    anulado_por = models.CharField(max_length=150, default=None)

    def __str__(self):
        return f"{self.produccion} anulado por {self.anulado_por} el {self.fecha_anulacion}"

class RegistroModificacion(models.Model):
    registro = models.ForeignKey(Registro_Produccion, on_delete=models.CASCADE)
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    datos_antes = models.TextField()
    fecha_modificacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Modificación de {self.registro} por {self.modificado_por} el {self.fecha_modificacion}"
    

    


