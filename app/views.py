from django.shortcuts import render
from .models import producto

# Create your views here.

def home(request):
    return render(request, 'index.html')
    

def listar_productos(request):
    productos = producto.objects.all()
    data = {
            'productos': productos
        }
    return render(request, 'productos.html', data)

