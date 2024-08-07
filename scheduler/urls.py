from django.urls import path
from . import views

urlpatterns = [
    path('calendar/<slug:calendar_slug>/', views.calendar_view, name='calendar_view'),
    path('event/create/', views.event_create, name='event_create'),
    # ...
    path('calendars/', views.calendar_view, name='calendar_view'),
    ## rendez-vus
    path('', views.calendar_list, name='calendar_list'),
    path('<str:calendar_slug>/', views.RendezvousCalendarView.as_view(), name='calendar'),
    path('<str:calendar_slug>/events/', views.RendezvousCalendarView.as_view(), name='calendar_events'),
]
