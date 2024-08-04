
from django import forms
from .models import CustomAppointment, CustomService, StaffMember, Availability, Conflict

class CustomAppointmentForm(forms.ModelForm):
    class Meta:
        model = CustomAppointment
        fields = ['client', 'service', 'phone', 'address', 'want_reminder', 'additional_info']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'want_reminder': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'additional_info': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CustomServiceForm(forms.ModelForm):
    class Meta:
        model = CustomService
        fields = ['name', 'duration', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['user', 'services']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['staff_member', 'day_of_week', 'start_time', 'end_time']
        widgets = {
            'staff_member': forms.Select(attrs={'class': 'form-control'}),
            'day_of_week': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class ConflictForm(forms.ModelForm):
    class Meta:
        model = Conflict
        fields = ['staff_member', 'date', 'start_time', 'end_time', 'reason']
        widgets = {
            'staff_member': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
        }