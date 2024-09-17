from django.contrib import admin
from schedule.models import Calendar, Event

class EventInline(admin.TabularInline):
    model = Event
    extra = 1  # Nombre de formulaires vides à afficher
    fields = ['title', 'start', 'end', 'color_event']

@admin.site.register(CalendarAdmin2)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    inlines = [EventInline]

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []
        return super(CalendarAdmin, self).get_inline_instances(request, obj)

