from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomAppointment, CustomService, StaffMember, Availability, Conflict
from .forms import CustomAppointmentForm, CustomServiceForm, StaffMemberForm, AvailabilityForm, ConflictForm

@login_required
def home(request):
    return render(request, 'home_page.html')



# Appointment views
@login_required
def appointment_list(request):
    appointments = CustomAppointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = CustomAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rendez-vous créé avec succès.')
            return redirect('rendezvous2:appointment_list')
    else:
        form = CustomAppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(CustomAppointment, pk=pk)
    if request.method == 'POST':
        form = CustomAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rendez-vous mis à jour avec succès.')
            return redirect('rendezvous2:appointment_list')
    else:
        form = CustomAppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(CustomAppointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Rendez-vous supprimé avec succès.')
        return redirect('rendezvous2:appointment_list')
    return render(request, 'appointment_confirm_delete.html', {'appointment': appointment})

# Service views
@login_required
def service_list(request):
    services = CustomService.objects.all()
    return render(request, 'service_list.html', {'services': services})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = CustomServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service créé avec succès.')
            return redirect('rendezvous2:service_list')
    else:
        form = CustomServiceForm()
    return render(request, 'service_form.html', {'form': form})

@login_required
def service_update(request, pk):
    service = get_object_or_404(CustomService, pk=pk)
    if request.method == 'POST':
        form = CustomServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service mis à jour avec succès.')
            return redirect('rendezvous2:service_list')
    else:
        form = CustomServiceForm(instance=service)
    return render(request, 'service_form.html', {'form': form})

@login_required
def service_delete(request, pk):
    service = get_object_or_404(CustomService, pk=pk)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service supprimé avec succès.')
        return redirect('rendezvous2:service_list')
    return render(request, 'service_confirm_delete.html', {'service': service})

# StaffMember views
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
            messages.success(request, 'Membre du personnel créé avec succès.')
            return redirect('rendezvous2:staff_member_list')
    else:
        form = StaffMemberForm()
    return render(request, 'staff_member_form.html', {'form': form})

@login_required
def staff_member_update(request, pk):
    staff_member = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        form = StaffMemberForm(request.POST, instance=staff_member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Membre du personnel mis à jour avec succès.')
            return redirect('rendezvous2:staff_member_list')
    else:
        form = StaffMemberForm(instance=staff_member)
    return render(request, 'staff_member_form.html', {'form': form})

@login_required
def staff_member_delete(request, pk):
    staff_member = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        staff_member.delete()
        messages.success(request, 'Membre du personnel supprimé avec succès.')
        return redirect('rendezvous2:staff_member_list')
    return render(request, 'staff_member_confirm_delete.html', {'staff_member': staff_member})

# Availability views
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
            messages.success(request, 'Disponibilité créée avec succès.')
            return redirect('rendezvous2:availability_list')
    else:
        form = AvailabilityForm()
    return render(request, 'availability_form.html', {'form': form})

@login_required
def availability_update(request, pk):
    availability = get_object_or_404(Availability, pk=pk)
    if request.method == 'POST':
        form = AvailabilityForm(request.POST, instance=availability)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disponibilité mise à jour avec succès.')
            return redirect('rendezvous2:availability_list')
    else:
        form = AvailabilityForm(instance=availability)
    return render(request, 'availability_form.html', {'form': form})

@login_required
def availability_delete(request, pk):
    availability = get_object_or_404(Availability, pk=pk)
    if request.method == 'POST':
        availability.delete()
        messages.success(request, 'Disponibilité supprimée avec succès.')
        return redirect('rendezvous2:availability_list')
    return render(request, 'availability_confirm_delete.html', {'availability': availability})

# Conflict views
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
            messages.success(request, 'Conflit créé avec succès.')
            return redirect('rendezvous2:conflict_list')
    else:
        form = ConflictForm()
    return render(request, 'conflict_form.html', {'form': form})

@login_required
def conflict_update(request, pk):
    conflict = get_object_or_404(Conflict, pk=pk)
    if request.method == 'POST':
        form = ConflictForm(request.POST, instance=conflict)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conflit mis à jour avec succès.')
            return redirect('rendezvous2:conflict_list')
    else:
        form = ConflictForm(instance=conflict)
    return render(request, 'conflict_form.html', {'form': form})

@login_required
def conflict_delete(request, pk):
    conflict = get_object_or_404(Conflict, pk=pk)
    if request.method == 'POST':
        conflict.delete()
        messages.success(request, 'Conflit supprimé avec succès.')
        return redirect('rendezvous2:conflict_list')
    return render(request, 'conflict_confirm_delete.html', {'conflict': conflict})