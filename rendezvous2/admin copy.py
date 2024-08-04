
from django.contrib import admin
from .models import CustomAppointment, CustomService, StaffMember, Availability, Conflict

@admin.register(CustomAppointment)
class CustomAppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'phone', 'want_reminder', 'paid', 'created_at')
    list_filter = ('want_reminder', 'paid', 'created_at')
    search_fields = ('client__username', 'phone', 'address')
    date_hierarchy = 'created_at'

@admin.register(CustomService)
class CustomServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')
    search_fields = ('name',)

@admin.register(StaffMember)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_services')
    search_fields = ('user__username',)

    def get_services(self, obj):
        return ", ".join([s.name for s in obj.services.all()])
    get_services.short_description = 'Services'

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('staff_member', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('day_of_week', 'staff_member')

@admin.register(Conflict)
class ConflictAdmin(admin.ModelAdmin):
    list_display = ('staff_member', 'date', 'start_time', 'end_time')
    list_filter = ('staff_member', 'date')
    search_fields = ('staff_member__user__username', 'reason')
    date_hierarchy = 'date'