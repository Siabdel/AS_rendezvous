from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from schedule.models import Calendar, Event
from .serializers import CalendarSerializer, EventSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = [IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Event.objects.all()
        calendar_slug = self.request.query_params.get('calendar_slug', None)
        if calendar_slug is not None:
            queryset = queryset.filter(calendar__slug=calendar_slug)
        return queryset

class CalendarEventsView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        calendar_slug = self.kwargs['calendar_slug']
        return Event.objects.filter(calendar__slug=calendar_slug)