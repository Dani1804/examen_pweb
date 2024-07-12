from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="/home"),
	path('home', views.home, name="home"),
    path('catalogoLibros', views.catalogoLibros, name="catalogoLibros"),
    path('catalogoAutores', views.catalogoAutores, name="catalogoAutores"),
    path('categorias', views.categorias, name="categorias"),
    path('verMas/', views.verMas, name="verMas"),
    path('buscar_libros/', views.buscar_libros, name='buscar_libros')
]
