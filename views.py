
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomAppointment
from .forms import CustomAppointmentForm

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = CustomAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('rendezvous2:appointment_list')
    else:
        form = CustomAppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})