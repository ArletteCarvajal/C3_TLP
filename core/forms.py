from django import forms
from .models import Registro_Produccion

class RegistroProduccionForm(forms.ModelForm):
    class Meta:
        model = Registro_Produccion
        fields = ['codigo_combustible', 'litros_produccion', 'fecha_produccion', 'turno', 'hora_registro', 'operador']



