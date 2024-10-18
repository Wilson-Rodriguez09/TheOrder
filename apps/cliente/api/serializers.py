from rest_framework.serializers import ModelSerializer
from apps.cliente.models import Cliente

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente

        fields = ['id','nombre']