from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('productos/', views.listar_productos, name="listar_productos"),
    path('contactos/', views.contacto, name="contacto"),
    path('agregar/', views.agregar_producto, name="agregar_producto"),
    path('listar/', views.listar_productos2, name="listar_productos2"),
    path('modificar/<id>/', views.modificar_producto, name="modificar_producto"),
]
