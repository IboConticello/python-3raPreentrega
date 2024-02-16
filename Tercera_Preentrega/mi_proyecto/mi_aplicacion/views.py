from django.shortcuts import render
from .forms import ClaseAForm, ClaseBForm, ClaseCForm
from .models import ClaseA, ClaseB, ClaseC

def formulario_insertar(request):
    if request.method == 'POST':
        form_a = ClaseAForm(request.POST)
        form_b = ClaseBForm(request.POST)
        form_c = ClaseCForm(request.POST)
        if form_a.is_valid() and form_b.is_valid() and form_c.is_valid():
            form_a.save()
            form_b.save()
            form_c.save()
    else:
        form_a = ClaseAForm()
        form_b = ClaseBForm()
        form_c = ClaseCForm()
    return render(request, 'formulario_insertar.html', {'form_a': form_a, 'form_b': form_b, 'form_c': form_c})

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        resultados_a = ClaseA.objects.filter(campo_a__icontains=query)
        resultados_b = ClaseB.objects.filter(campo_b__icontains=query)
        resultados_c = ClaseC.objects.filter(campo_c__icontains=query)
        return render(request, 'resultado_busqueda.html', {'resultados_a': resultados_a, 'resultados_b': resultados_b, 'resultados_c': resultados_c})
    return render(request, 'buscar.html')

def resultado_busqueda(request):
    return render(request, 'resultado_busqueda.html')

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')