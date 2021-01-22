from django.shortcuts import render
from .models import producto
from .forms import contactoForm, productoForm

# Create your views here.

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

    