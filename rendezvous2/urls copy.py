
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'rendezvous2'

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/update/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('services/', views.service_list, name='service_list'),
    path('customers/', views.customer_list, name='customer_list'),
]


app_name = 'rendezvous2'

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:pk>/update/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('staff-members/', views.staff_member_list, name='staff_member_list'),
    path('staff-members/create/', views.staff_member_create, name='staff_member_create'),
    path('availabilities/', views.availability_list, name='availability_list'),
    path('availabilities/create/', views.availability_create, name='availability_create'),
    path('conflicts/', views.conflict_list, name='conflict_list'),
    path('conflicts/create/', views.conflict_create, name='conflict_create'),
    path('api/', include(router.urls)),
]