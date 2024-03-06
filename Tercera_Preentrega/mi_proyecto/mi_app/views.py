from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mi_app.models import *
from mi_app.forms import ClienteForm, ProductoForm, EnvioForm, FormularioRegistroUsuario, FormularioCambioPassword, FormularioEdicion
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 

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
            cliente = Cliente (nombre=nombre, apellido=apellido,correo=correo)
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
            producto = Producto (nombre=nombre, descripcion=descripcion,precio=precio)
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
            calle = info['calle']
            altura = info['altura']
            ciudad = info['ciudad']
            envio = Envio (calle=calle, altura=altura,ciudad=ciudad)
            envio.save()
            return render(request, "inicio.html")
    else:
        form = EnvioForm()
    return render(request, "envio.html", {"formulario":form})


### busqueda ###

def busqueda_cliente_view(request):
    return render(request, "busquedaCliente.html")


def buscar(request):
    correo = request.GET.get('correo')
    if correo:
        clientes = Cliente.objects.filter(correo__icontains=correo)
        return render(request, "resultadoBusqueda.html", {"clientes": clientes})
    else:
        return render(request, "resultadoBusqueda.html", {"clientes": None})
    

########################################################

class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')

class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'passwordExitoso.html', {})


