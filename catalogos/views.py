from django.shortcuts import render
from .models import *

# Create your views here.

def home (request):
    Navbars = NavItem.objects.all()
    context = {
        "Navbars": Navbars,
        
    }
    
    return render(request,'catalogos/home.html',context)

def catalogoLibros (request):
    Navbars = NavItem.objects.all()
    Libros = Libro.objects.all()
    context = {
        "Navbars": Navbars,
        "Libros": Libros  
    }
    return render(request,'catalogos/catalogoLibros.html',context)

def catalogoAutores (request):
    Navbars = NavItem.objects.all()
    Autores = Autor.objects.all()
    context = {
        "Navbars": Navbars,
        "Autores": Autores
        
    }
    return render(request,'catalogos/catalogoAutores.html',context)

def categorias (request):
    Navbars = NavItem.objects.all()
    Categorias = Categoria.objects.all()
    context = {
        "Navbars": Navbars,
        "Categorias": Categorias
        
    }
    return render(request,'catalogos/categorias.html',context)