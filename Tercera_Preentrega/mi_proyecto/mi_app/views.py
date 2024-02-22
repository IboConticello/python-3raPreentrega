from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mi_app.models import *
from mi_app.forms import ClienteForm, ProductoForm, EnvioForm

def inicio(request):

    return render(request,'inicio.html')


def cliente_form_view(request):


    if request.method == "POST":

        form=ClienteForm(request.POST)  
        print(form)
        if form.is_valid():

            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            correo = info['correo']
            cliente = ClienteForm (nombre=nombre, apellido=apellido,correo=correo)
            cliente.save()
            return render(request, "inicio.html")

    else:
        form = ClienteForm()
    return render(request, "cliente.html", {"formulario":form})
    
def producto_form_view(request):


    if request.method == "POST":

        form=ProductoForm(request.POST)  
        print(form)
        if form.is_valid():

            info = form.cleaned_data
            nombre = info['nombre']
            descripcion = info['descripcion']
            precio = info['precio']
            producto = ProductoForm (nombre=nombre, descripcion=descripcion,precio=precio)
            producto.save()
            return render(request, "inicio.html")

    else:
        form = ProductoForm()
    return render(request, "cliente.html", {"formulario":form})


def envio_form_view(request):
    if request.method == "POST":
        form=EnvioForm(request.POST)  
        print(form)
        if form.is_valid():
            info = form.cleaned_data
            calle = info('calle')
            altura = info('altura')
            ciudad = info('ciudad')
            envio = EnvioForm (calle=calle, altura=altura,ciudad=ciudad)
            envio.save()
            return render(request, "mi_app/inicio.html")
    else:
        form = EnvioForm()
    return render(request, "mi_app/envio.html", {"formulario":form})
