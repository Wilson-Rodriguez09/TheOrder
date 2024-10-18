from django.db import models

# Create your models here.


class Producto(models.Model):
    
    nombre_producto = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_producto
