from django.db import models


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    duracion = models.IntegerField()
    sinopsis = models.TextField()
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre