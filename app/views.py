from django.shortcuts import render
from .models import producto
from django.http.response import JsonResponse



# Create your views here.


def index(request):
    return render(request, 'SemaforoCaloriasConJSVanilla.html')

def list_productos(request):
    productos=list(producto.objects.values())
    data= {'producto': productos}
    return JsonResponse(data)    



