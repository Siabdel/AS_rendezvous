
from rest_framework.routers import DefaultRouter
from .api_views import CustomerViewSet, ServiceViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)