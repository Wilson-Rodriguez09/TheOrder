from rest_framework.viewsets import ModelViewSet
from apps.pedidos.models import Pedidos
from apps.pedidos.api.serializers import PedidosSerializer

class PedidosModelViewSet(ModelViewSet):
    serializer_class = PedidosSerializer
    queryset = Pedidos.objects.all()

