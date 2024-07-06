from rest_framework import serializers
from .models import Operador, Plantas, Productos, Registro_Produccion

class OperadorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = '__all__'
 
class PlantasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Plantas
        fields = '__all__'
    
class ProductosSerializer (serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class Registro_ProduccionsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Registro_Produccion
        fields = '__all__'