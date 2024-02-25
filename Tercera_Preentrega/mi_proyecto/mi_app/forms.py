from django import forms



class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    correo = forms.EmailField()

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)
    precio = forms.IntegerField()

class EnvioForm(forms.Form):
    calle = forms.CharField(max_length=70)
    altura = forms.IntegerField()
    ciudad = forms.CharField(max_length=20)
