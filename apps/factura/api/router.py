from rest_framework.routers import DefaultRouter
from apps.factura.api.views import FacturaModelViewSet

router_factura = DefaultRouter()
router_factura.register(prefix="factura", basename="factura", viewset=FacturaModelViewSet)