from django.contrib import admin
from django.urls import path, include
from .views import productoViewset,home,listar_productos,contacto,agregar_producto,listar_productos2,modificar_producto,eliminar_producto,somos1
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', productoViewset)

#
urlpatterns = [
    path('', home, name="home"),
    path('productos/', listar_productos, name="listar_productos"),
    path('contactos/', contacto, name="contacto"),
    path('agregar/', agregar_producto, name="agregar_producto"),
    path('listar/', listar_productos2, name="listar_productos2"),
    path('modificar/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar/<id>/', eliminar_producto, name="eliminar_producto"),   
    path('api/', include(router.urls)),
    path('somos/', somos1, name="somos1"),
]
