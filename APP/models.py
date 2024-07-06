from django.db import models

# Create your models here.

class Operador (models.Model):  #modelo solo con los nombres de los operadores
        nombre = models.CharField(max_length = 100)


class Plantas (models.Model):    #modelo de plantas con sus nombres y contraccion
        nomnbre = models.CharField(max_length = 100)
        codigo = models.CharField(max_length = 100)

class Productos (models.Model): #modelo de productos, contraccion o codigo y la planta de donde proviene
        nombre = models.CharField(max_length = 100)
        codigo = models.CharField(max_length = 3, primary_key = True)
        planta = models.ForeignKey(Plantas, on_delete = models.CASCADE)

class Registro_Produccion (models.Model):
        codigo_combustible = models.ForeignKey(Productos, on_delete = models.CASCADE)
        litros_produccion = models.FloatField()
        fecha_produccion = models.DateField()
        turno = models.CharField(max_length = 6, choices = [('mañana','AM'), ('tarde','PM'), ('noche','MM')])
        hora_registro = models.TimeField()
        operador = models.ForeignKey(Operador, on_delete = models.CASCADE)

