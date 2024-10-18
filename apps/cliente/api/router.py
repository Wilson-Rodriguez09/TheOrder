from rest_framework.routers import DefaultRouter
from apps.cliente.api.views import ClienteModelViewSet

router_cliente = DefaultRouter()
router_cliente.register(prefix="cliente", basename="cliente", viewset=ClienteModelViewSet)