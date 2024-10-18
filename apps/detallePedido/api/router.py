from rest_framework.routers import DefaultRouter
from apps.detallePedido.api.views import DetalleModelViewsSet


router_detalle = DefaultRouter()
router_detalle.register(prefix="detalle", basename="detalle", viewset=DetalleModelViewsSet)