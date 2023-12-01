from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='SemaforoCaloriasConJSVanilla'),
    path('list_productos/',views.list_productos,name='list_productos'),
    path('registrarproducto/', views.index)
]

