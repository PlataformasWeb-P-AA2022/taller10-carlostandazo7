from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import Parroquia, Barrio

# importar los formularios de forms.py
from ordenamiento.forms import *

# Generar una vista que liste las parroquias y sus barrios

def index(request):
	parroquias = Parroquia.objects.all()

	informacion_template = {'parroquias': parroquias,
	'num_parroquias': len(parroquias)}

	return render(request, 'index.html', informacion_template)

# Generar una vista que liste los barrios

def listaBarrios(request):
	barrios = Barrio.objects.all()

	informacion_template = {'barrios':barrios}

	return render(request, 'listaBarrios.html', informacion_template)

# Generar un formulario que cree una parroquia

def crearParroquia(request):
	if request.method == 'POST':
		formulario = ParroquiaForm(request.POST)
		print(formulario.errors)
		if formulario.is_valid():
			formulario.save()
			return redirect(index)
	else:
		formulario = ParroquiaForm()

	diccionario = {'formulario': formulario}

	return render(request, 'crearParroquia.html', diccionario)

# Generar un formulario que cree un barrio de una parroquia

def crearBarrioDeParroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)

    diccionario = {'formulario': formulario, 'parroquia':parroquia}

    return render(request, 'crearBarrioDeParroquia.html', diccionario)

# Generar un formulario que edite una parroquia

def editarParroquia(request, id):
	parroquia = Parroquia.objects.get(pk=id)
	if request.method == 'POST':
		formulario = ParroquiaForm(request.POST, instance=parroquia)
		print(formulario.errors)
		if formulario.is_valid():
			formulario.save()
			return redirect(index)
	else:
		formulario = ParroquiaForm(instance=parroquia)

	diccionario = {'formulario': formulario}

	return render(request, 'editarParroquia.html', diccionario)

# Generar un formulario que edite un barrio

def editarBarrio(request, id):
	barrio = Barrio.objects.get(pk=id)
	if request.method == 'POST':
		formulario = BarrioForm(request.POST, instance=barrio)
		print(formulario.errors)
		if formulario.is_valid():
			formulario.save()
			return redirect(index)
	else:
		formulario = BarrioForm(instance=barrio)

	diccionario = {'formulario': formulario}

	return render(request, 'editarBarrio.html', diccionario)