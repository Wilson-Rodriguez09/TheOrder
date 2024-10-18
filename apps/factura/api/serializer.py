from rest_framework.serializers import ModelSerializer
from apps.factura.models import Factura

class FacturaSerializer(ModelSerializer):
    class Meta:
        model = Factura

        fields = ['id','pedido','monto_total']