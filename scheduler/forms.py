from django import forms
from schedule.models import Event, Calendar

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start', 'end', 'calendar']
