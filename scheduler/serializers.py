from rest_framework import serializers
from schedule.models import Calendar, Event, Occurrence

# events/serializers.py
class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'name', 'slug']


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ['id', 'start', 'end', 'event', 'original_start', 'original_end']

class EventSerializer(serializers.ModelSerializer):
    occurrences = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'start', 'end', 'creator', 'calendar', 'color_event', 'occurrences']

    def get_occurrences(self, obj):
        occurrences = obj.get_occurrences(obj.start, obj.end_recurring_period)
        return OccurrenceSerializer(occurrences, many=True).data
