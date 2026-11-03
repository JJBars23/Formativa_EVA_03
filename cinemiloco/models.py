from django.db import models


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    duracion = models.IntegerField()
    sinopsis = models.TextField()
    genero = models.ForeignKey('Genero', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.titulo

    

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre


class tickets(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} tickets for {self.pelicula.titulo}"