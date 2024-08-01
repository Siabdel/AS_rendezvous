
from django.urls import path, include
from .routes import router
from rendezvous import views

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='home'),
    path('appointments/', views.AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/new/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointments/<int:pk>/edit/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('api/', include(router.urls)),
]