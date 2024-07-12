from django.shortcuts import render
from .models import *
from django.http import JsonResponse

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

def categorias(request):
    Navbars = NavItem.objects.all()
    Categorias = Categoria.objects.all()
    Libros = Libro.objects.all().select_related('id_autor' , 'id_categoria') 
    context = {
        "Navbars": Navbars,
        "Categorias": Categorias,
        "Libros": Libros,
    }
    return render(request, 'catalogos/categorias.html', context)

def verMas(request):
    Navbars = NavItem.objects.all()
    id_libro = request.GET.get('id_libro')
    Libros = Libro.objects.get(id_libro=id_libro)
    Autor = Libros.id_autor
    Categoria = Libros.id_categoria

    context = {
        
        "Navbars": Navbars,
        "Libros": Libros,
        "Autor": Autor,
        "Categoria": Categoria
    }
    return render(request,'catalogos/verMas.html',context) 


def buscar_libros(request):
    libros = Libro.objects.all()

    buscar_libro = request.GET.get('buscarLibro', '')
    categoria_nombre = request.GET.get('categoria', '')

    if buscar_libro:
        libros = libros.filter(titulo__icontains=buscar_libro)

    if categoria_nombre:
        libros = libros.filter(id_categoria__nombre=categoria_nombre)

    libros_data = [{
        'id_libro': libro.id_libro,
        'titulo': libro.titulo,
        'ano_de_publicacion': libro.ano_de_publicacion,
        'nombre_autor': libro.id_autor.nombre,
        'categoria': libro.id_categoria.nombre,
        'descripcion_breve': libro.descripcion_breve,
    } for libro in libros]

    return JsonResponse({'libros': libros_data})