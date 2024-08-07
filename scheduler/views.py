from django.shortcuts import render, redirect
from schedule.models import Calendar, Event
from django.views.generic import TemplateView
from schedule.views import CalendarByPeriodsView
from .forms import EventForm

class RendezvousCalendarView(CalendarByPeriodsView):
    template_name = 'rendezvous/calendar.html'

def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'rendezvous/calendar_list.html', {'calendars': calendars})


def calendar_view(request, calendar_slug):
    calendar = Calendar.objects.get(slug=calendar_slug)
    events = Event.objects.filter(calendar=calendar)
    return render(request, 'calendar.html', {'calendar': calendar, 'events': events})



def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view', calendar_slug=form.cleaned_data['calendar'].slug)
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})
