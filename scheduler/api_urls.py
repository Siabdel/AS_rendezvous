from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CalendarViewSet, EventViewSet
from . import api_views as views

router = DefaultRouter()
router.register(r'calendars', CalendarViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Gardez vos autres URLs ici
    path('calendars/<str:calendar_slug>/events/', views.CalendarEventsView.as_view(), name='calendar-events'),
]
