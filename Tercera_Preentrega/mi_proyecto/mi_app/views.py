from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from mi_app.models import *
from mi_app.models import Libros, Comentario
from mi_app.forms import ActualizacionLibros, FormularioCambioPassword, FormularioEdicion, FormularioRegistroUsuario, FormularioComentario, FormularioNuevoLibros
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 

def inicio(request):
    return render(request,'inicio.html')


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

@login_required
def signout(request):
    logout(request)
    return redirect('inicio')

# Libro Romance

class RomanceLista(LoginRequiredMixin, ListView):
    context_object_name = 'romances'
    queryset = Libros.objects.filter(libros__startswith='romance')
    template_name = 'listaRomance.html'
    login_url = '/login/'

class RomanceDetalle(LoginRequiredMixin, DetailView):
    model = Libros
    context_object_name = 'romance'
    template_name = 'romanceDetalle.html'

class RomanceUpdate(LoginRequiredMixin, UpdateView):
    model = Libros
    form_class = ActualizacionLibros
    success_url = reverse_lazy('romance')
    context_object_name = 'romance'
    template_name = 'romanceEdicion.html'

class RomanceDelete(LoginRequiredMixin, DeleteView):
    model = Libros
    success_url = reverse_lazy('romance')
    context_object_name = 'romance'
    template_name = 'romanceBorrado.html'

# Libro Fantasia

class FantasiaLista(LoginRequiredMixin, ListView):
    context_object_name = 'fantasias'
    queryset = Libros.objects.filter(libros__startswith='fantasia')
    template_name = 'listaFantasia.html'
    login_url = '/login/'

class FantasiaDetalle(LoginRequiredMixin, DetailView):
    model = Libros
    context_object_name = 'fantasia'
    template_name = 'fantasiaDetalle.html'

class FantasiaUpdate(LoginRequiredMixin, UpdateView):
    model = Libros
    form_class = ActualizacionLibros
    success_url = reverse_lazy('fantasia')
    context_object_name = 'fantasia'
    template_name = 'fantasiaEdicion.html'

class FantasiaDelete(LoginRequiredMixin, DeleteView):
    model = Libros
    success_url = reverse_lazy('fantasia')
    context_object_name = 'fantasia'
    template_name = 'fantasiaBorrado.html'


# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# CREACION LIBROS

class LibrosCreacion(LoginRequiredMixin, CreateView):
    model = Libros
    form_class = FormularioNuevoLibros
    success_url = reverse_lazy('inicio')
    template_name = 'librosCreacion.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LibrosCreacion, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'acercaDeMi.html', {})
