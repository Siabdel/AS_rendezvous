from django.urls import path
from . import views

app_name="scheduler"

urlpatterns = [
    # fullcalendar
    path('', views.fullcalendar, name='fullcalendar'),
    path('calendar/<slug:calendar_slug>/', views.calendar_view, name='calendar_view'),
    path('event/create/', views.event_create, name='event_create'),
    # ...
    path('calendars/', views.calendar_view, name='calendar_view'),
    ## rendez-vus
    path('list/', views.calendar_list, name='calendar_list'),
    path('<str:calendar_slug>/', views.RendezvousCalendarView.as_view(), name='calendar'),
    path('<str:calendar_slug>/events/', views.RendezvousCalendarView.as_view(), name='calendar_events'),
]
