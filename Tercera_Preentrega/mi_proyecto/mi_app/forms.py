from django import forms
from .models import ClienteForm, ProductoForm, EnvioForm


class ClienteForm(forms.ModelForm):
    model = ClienteForm
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo = forms.EmailField()

class ProductoForm(forms.ModelForm):
    model = ProductoForm
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)
    precio = forms.IntegerField()

class EnvioForm(forms.ModelForm):
    model = EnvioForm
    calle = forms.CharField(max_length=70)
    altura = forms.IntegerField()
    ciudad = forms.CharField(max_length=20)
