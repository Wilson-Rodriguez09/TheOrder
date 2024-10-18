from rest_framework.viewsets import ModelViewSet
from apps.detallePedido.api.serializer import DetalleSerializer
from apps.detallePedido.models import Detalle


class DetalleModelViewsSet(ModelViewSet):
    serializer_class =  DetalleSerializer
    queryset = Detalle.objects.all()