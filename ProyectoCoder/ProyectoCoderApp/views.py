import datetime

from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso, Estudiante, Profesor
from .forms import NuevoCurso, NuevoEstudiante, NuevoProfesor
from django.db.models import Q

from django.shortcuts import redirect

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

def crear_curso(request):

    #post
    if request.method == 'POST':

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso=formulario.cleaned_data

            curso = Curso(nombre=info_curso["nombre"], comision=int(info_curso["comision"]))

            curso.save() #guardamos en la base de datos

            return redirect("cursos")
        else:
            redirect("crear_curso")

    else: #get y otros

        formularioVacio = NuevoCurso()

        return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formularioVacio})


def agregar_profesor(request):

    #post
    if request.method == 'POST':

        formulario = NuevoProfesor(request.POST)

        if formulario.is_valid():

            info_profe=formulario.cleaned_data

            profesor = Profesor(nombre=info_profe["nombre"], apellido=info_profe["apellido"])

            profesor.save() #guardamos en la base de datos

            return redirect("profesores")
        else:
            redirect("agregar_profesor")

    else: #get y otros

        formularioVacio = NuevoProfesor()

        return render(request,"ProyectoCoderApp/agregar_profesor.html",{"form":formularioVacio})



def agregar_estudiante(request):

    #post
    if request.method == 'POST':

        formulario = NuevoEstudiante(request.POST)

        if formulario.is_valid():

            info_estudiante=formulario.cleaned_data

            estudiante = Estudiante(nombre=info_estudiante["nombre"], apellido=info_estudiante["apellido"])

            estudiante.save() #guardamos en la base de datos

            return redirect("estudiantes")
        else:
            redirect("agregar_estudiante")

    else: #get y otros

        formularioVacio = NuevoEstudiante()

        return render(request,"ProyectoCoderApp/agregar_estudiante.html",{"form":formularioVacio})



def buscar_comision(request):

    if request.method == "POST":

        comision=request.POST["comision"]

        comisiones = Curso.objects.filter(comision__icontains=comision)

        return render(request,"ProyectoCoderApp/buscar_comision.html", {"comisiones":comisiones})
    
    else:

        comisiones = [] #Curso.objects.all()

    return render(request,"ProyectoCoderApp/buscar_comision.html", {"comisiones":comisiones}) 

def profesores(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search !="":
            profesores = Profesor.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search)).values()

            return render(request, "ProyectoCoderApp/profesores.html", {"profesores":profesores, "search":True, "busqueda":search})

    profesores = Profesor.objects.all()

    return render(request,"ProyectoCoderApp/profesores.html",{"profesores":profesores})

def estudiantes(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search !="":
            estudiantes = Estudiante.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search)).values()

            return render(request, "ProyectoCoderApp/estudiantes.html", {"estudiantes":estudiantes, "search":True, "busqueda":search})

    estudiantes = Estudiante.objects.all()

    return render(request,"ProyectoCoderApp/estudiantes.html",{"estudiantes":estudiantes})

def cursos(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search !="":
            cursos = Curso.objects.filter( Q(nombre__icontains=search) | Q(comision__icontains=search)).values()

            return render(request, "ProyectoCoderApp/cursos.html", {"cursos":cursos, "search":True, "busqueda":search})
    
    cursos = Curso.objects.all()

    return render(request,"ProyectoCoderApp/cursos.html",{"cursos":cursos})


def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")