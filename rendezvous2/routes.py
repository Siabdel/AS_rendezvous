
from rest_framework.routers import DefaultRouter
from rendezvous2 import api_views

router = DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'customers', api_views.CustomerViewSet)
router.register(r'appointments', api_views.CustomAppointmentViewSet)
router.register(r'services', api_views.CustomServiceViewSet)
router.register(r'staff-members', api_views.StaffMemberViewSet)
router.register(r'availabilities', api_views.AvailabilityViewSet)
router.register(r'conflicts', api_views.ConflictViewSet)
