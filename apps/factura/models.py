from django.db import models
from apps.pedidos.models import Pedidos
# Create your models here.

class Factura(models.Model):

    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    monto_total = models.FloatField()
