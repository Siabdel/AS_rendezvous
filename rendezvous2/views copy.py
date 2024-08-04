
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomAppointment, CustomService, StaffMember, Availability, Conflict
from .forms import CustomAppointmentForm, StaffMemberForm, AvailabilityForm, ConflictForm

@login_required
def staff_member_list(request):
    staff_members = StaffMember.objects.all()
    return render(request, 'staff_member_list.html', {'staff_members': staff_members})

@login_required
def staff_member_create(request):
    if request.method == 'POST':
        form = StaffMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rendezvous2:staff_member_list')
    else:
        form = StaffMemberForm()
    return render(request, 'staff_member_form.html', {'form': form})

@login_required
def availability_list(request):
    availabilities = Availability.objects.all()
    return render(request, 'availability_list.html', {'availabilities': availabilities})

@login_required
def availability_create(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rendezvous2:availability_list')
    else:
        form = AvailabilityForm()
    return render(request, 'availability_form.html', {'form': form})

@login_required
def conflict_list(request):
    conflicts = Conflict.objects.all()
    return render(request, 'conflict_list.html', {'conflicts': conflicts})

@login_required
def conflict_create(request):
    if request.method == 'POST':
        form = ConflictForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rendezvous2:conflict_list')
    else:
        form = ConflictForm()
    return render(request, 'conflict_form.html', {'form': form})