from django import forms
from .models import Registro_Produccion, Operador, Supervisor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class RegistroProduccionForm(forms.ModelForm):
    class Meta:
        model = Registro_Produccion
        fields = ['codigo_combustible', 'litros_produccion', 'turno']  

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    

#formulario registro
    
class SupervisorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OperadorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





