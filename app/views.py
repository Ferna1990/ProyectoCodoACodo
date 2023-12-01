from django.shortcuts import render, redirect
from .models import producto
from django.http.response import JsonResponse



# Create your views here.


def index(request):
    return render(request, 'SemaforoCaloriasConJSVanilla.html')

def list_productos(request):
    productos=list(producto.objects.values())
    data= {'producto': productos}
    return JsonResponse(data)    

def registrarProducto(request):
    Nombre=request.POST['txtnombre']
    Calorias=request.POST['txtcalorias']
    Color=request.POST['txtcolor']
    Producto = producto.objects.create(Nombre=Nombre, Calorias=Calorias, Color=Color)
    return redirect('/')



