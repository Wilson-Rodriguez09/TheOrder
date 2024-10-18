from rest_framework.viewsets import ModelViewSet
from apps.producto.models import Producto
from apps.producto.api.serializers import ProductoSerializer

class ProductoModelViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

