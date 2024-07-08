from django.db import models

# Create your models here.
class Libro(models.Model):
    id_libro = models.AutoField(db_column="idLibro", primary_key=True)
    titulo = models.CharField(max_length=200)
    ano_de_publicacion = models.IntegerField()
    descripcion_breve = models.TextField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    id_autor = models.AutoField(db_column="idAutor",primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column="idCategoria", primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class NavItem(models.Model):
    id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
    titulo = models.CharField(max_length=100)
    url = models.URLField()


