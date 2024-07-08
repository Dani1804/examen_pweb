from django.urls import path, include
from . import views

urlpatterns = [
	path('home', views.home, name="home"),
    path('catalogoLibros', views.catalogoLibros, name="catalogoLibros"),
    path('catalogoAutores', views.catalogoAutores, name="catalogoAutores"),
    path('categorias', views.categorias, name="categorias")
]
