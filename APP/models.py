from django.db import models

# Create your models here.

class Operador (models.Model):  #modelo solo con los nombres de los operadores
        nombre_operador = models.CharField(max_length = 100)

        #funcion para que en las tablas de la BBDD se vean los nombres y no como object
        def __str__(self):
                return self.nombre_operador

class Plantas (models.Model):    #modelo de plantas con sus nombres y contraccion
        nombre_planta = models.CharField(max_length = 100)
        codigo_planta = models.CharField(max_length = 100)

class Productos (models.Model): #modelo de productos, contraccion o codigo y la planta de donde proviene
        nombre_producto = models.CharField(max_length = 100)
        codigo_producto = models.CharField(max_length = 3, primary_key = True)
        nombre_planta = models.ForeignKey(Plantas, on_delete = models.CASCADE)

        def _str_(self):
                return f'{self.nombre_producto} - {self.codigo_producto} - {self.nombre_planta.nombre_planta}'

class Registro_Produccion (models.Model):
        codigo_combustible = models.ForeignKey(Productos, on_delete = models.CASCADE)
        litros_produccion = models.FloatField()
        fecha_produccion = models.DateField()
        turno = models.CharField(max_length = 6, choices = [('mañana','AM'), ('tarde','PM'), ('noche','MM')])
        hora_registro = models.TimeField()
        operador = models.ForeignKey(Operador, on_delete = models.CASCADE)

        def _str_(self):
                return f'{self.codigo_combustible.codigo_producto} - {self.litros_produccion} - {self.fecha_produccion} - {self.turno} - {self.hora_registro} - {self.operador.nombre_operador}'