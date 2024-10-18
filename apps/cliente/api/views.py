from rest_framework.viewsets import ModelViewSet
from apps.cliente.models import Cliente
from apps.cliente.api.serializers import ClienteSerializer

class ClienteModelViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()