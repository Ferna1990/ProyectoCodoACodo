from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.


def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Producto listados!')
    return render(request, "gestionProducto.html", {"cursos": cursosListados})


def registrarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Producto registrado!')
    return redirect('/')


def edicionProducto(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"curso": curso})


def editarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, 'Producto actualizado!')

    return redirect('/')


def eliminarProducto(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/')
