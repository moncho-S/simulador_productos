from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def inicio(request):
    context={}
    return render(request,'inicio.html',context)
def mostrar_lab(request):
    laboratorios=Laboratorio.objects.all()
    num_visits = request.session.get('num_visits', 0) 
    request.session['num_visits'] = num_visits + 1
    context={
        'laboratorios':laboratorios,
        'num_visits':num_visits
        }
    return render(request,'mostrar.html',context)

def insertar_lab(request):
    context={}
    if request.method=="POST":
        lab_nombre=request.POST['lab_nombre']
        lab_ciudad=request.POST['lab_ciudad']
        lab_pais=request.POST['lab_pais']
        labo=Laboratorio(nombre=lab_nombre,
                         ciudad=lab_ciudad,
                         pais=lab_pais)
        labo.save()
        return redirect('../mostrar/')
    else:
        return render(request,'insertar.html',context)


def editar_lab(request,pk):
    labo=Laboratorio.objects.get(id=pk)
    context={
        'laboratorio':labo
        }
    return render(request,'editar.html',context)

def actualizar_lab(request,pk):
    lab_nombre = request.POST['lab_nombre'] 
    lab_ciudad = request.POST['lab_ciudad'] 
    lab_pais = request.POST['lab_pais'] 
    labo = Laboratorio.objects.get(id=pk) 
    labo.nombre = lab_nombre 
    labo.ciudad = lab_ciudad 
    labo.pais = lab_pais  
    labo.save() 
    return redirect('../mostrar/')

def eliminar_lab(request,pk):
    labo = Laboratorio.objects.get(id=pk) 
    if request.method == 'POST': 
        labo.delete() 
        return redirect('../mostrar/') 
    context = { 
        'laboratorio': labo,
        } 
    return render(request, 'eliminar.html', context)