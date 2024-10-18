from rest_framework.serializers import ModelSerializer
from apps.detallePedido.models import Detalle


class DetalleSerializer(ModelSerializer):
    class Meta:
        model= Detalle

        fields = ['id','cliente', 'pedidos', 'cantidad', 'observaciones']