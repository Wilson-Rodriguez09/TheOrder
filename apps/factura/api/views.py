from rest_framework.viewsets import ModelViewSet
from apps.factura.api.serializer import FacturaSerializer
from apps.factura.models import Factura

class FacturaModelViewSet(ModelViewSet):
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all()