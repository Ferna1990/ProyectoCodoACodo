from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.


def home(request):
    productosListados = Curso.objects.all()
    messages.success(request, '¡Producto listados!')
    return render(request, "gestionProducto.html", {"cursos": productosListados})


def registrarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    producto = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Producto registrado!')
    return redirect('/')


def edicionProducto(request, codigo):
    producto = Curso.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"curso": producto})


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
    producto = Curso.objects.get(codigo=codigo)
    producto.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/')
