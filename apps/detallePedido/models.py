from django.db import models
from apps.cliente.models import Cliente
from apps.pedidos.models import Pedidos
# Create your models here.

class Detalle(models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    pedidos = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    observaciones = models.TextField(max_length=600)
