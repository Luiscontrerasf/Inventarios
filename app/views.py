from django.shortcuts import render, redirect, get_object_or_404
from .models import producto
from .forms import contactoForm, productoForm 
from rest_framework import viewsets
from .serializers import productoSerializer



# Create your views here.

class productoViewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = productoSerializer



def somos1(request):
    return render(request, 'somos.html')


def home(request):
    return render(request, 'index.html')
    

def listar_productos(request):
    productos = producto.objects.all()
    data = {
            'productos': productos
        }
    return render(request, 'productos.html', data)


def contacto(request):
    data = {
        'form': contactoForm()
    }

    if request.method == 'POST':
        formulario = contactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario    

    return render(request, 'contactos.html', data)


def agregar_producto(request):
    
    data = {
        'form': productoForm()
    }

    if request.method == 'POST':
        formulario = productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Agregado correctamente"
        else:
            data["form"] = formulario  

    return render(request, 'agregar.html', data)

def listar_productos2(request):
    productos2 = producto.objects.all()

    data = {
            'productos2': productos2
    }    
    return render(request, 'listar.html', data)


def modificar_producto(request, id):
    
    productos = get_object_or_404(producto, id=id)

    data = {
        'form' : productoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = productoForm(data=request.POST, instance=productos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario  
    
    return render(request, 'modificar.html', data)    


def eliminar_producto(request, id):
    productos = get_object_or_404(producto, id=id)
    productos.delete()
    return redirect(to="listar_productos")
    
    