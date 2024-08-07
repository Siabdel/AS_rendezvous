
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

app_name = 'rendezvous2'

# Router for API views
router = DefaultRouter()
router.register(r'appointments', api_views.CustomAppointmentViewSet)
router.register(r'services', api_views.CustomServiceViewSet)
router.register(r'staff-members', api_views.StaffMemberViewSet)
router.register(r'availabilities', api_views.AvailabilityViewSet)
router.register(r'conflicts', api_views.ConflictViewSet)

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # ... autres URLs ...
    # Appointments
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/update/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),

    # Services
    path('services/', views.service_list, name='service_list'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/update/', views.service_update, name='service_update'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),

    # Staff Members
    path('staff-members/', views.staff_member_list, name='staff_member_list'),
    path('staff-members/create/', views.staff_member_create, name='staff_member_create'),
    path('staff-members/<int:pk>/update/', views.staff_member_update, name='staff_member_update'),
    path('staff-members/<int:pk>/delete/', views.staff_member_delete, name='staff_member_delete'),

    # Availabilities
    path('availabilities/', views.availability_list, name='availability_list'),
    path('availabilities/create/', views.availability_create, name='availability_create'),
    path('availabilities/<int:pk>/update/', views.availability_update, name='availability_update'),
    path('availabilities/<int:pk>/delete/', views.availability_delete, name='availability_delete'),

    # Conflicts
    path('conflicts/', views.conflict_list, name='conflict_list'),
    path('conflicts/create/', views.conflict_create, name='conflict_create'),
    path('conflicts/<int:pk>/update/', views.conflict_update, name='conflict_update'),
    path('conflicts/<int:pk>/delete/', views.conflict_delete, name='conflict_delete'),
    # fullcalendar
    path('fullcalendar/', views.fullcalendar, name='fullcalendar'),
    
    # API URLs
    path('api/', include(router.urls)),
]