from django.db import models
from apps.cliente.models import Cliente
# Create your models here.

class Pedidos(models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null = True)
    OPTION_CHOISES=[('Para Llevar', 'Para Llevar'),('Consumir','Consumir')]
    ESTADO_CHOICES=[('En espera', 'En espera'),('En preparacion','En preparacion'),('Listo','Listo')]
    option = models.CharField(max_length=50, choices= OPTION_CHOISES ,default='Para Llevar')
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='En espera')


    def __str__(self):
        return self.cliente
