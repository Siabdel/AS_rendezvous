
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer, Service, Appointment
from .forms import AppointmentForm
from datetime import datetime, timedelta

class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(user=self.user, phone='1234567890')

    def test_customer_creation(self):
        self.assertTrue(isinstance(self.customer, Customer))
        self.assertEqual(self.customer.__str__(), self.user.username)

class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name='Test Service', duration=timedelta(hours=1), price=100.00)

    def test_service_creation(self):
        self.assertTrue(isinstance(self.service, Service))
        self.assertEqual(self.service.__str__(), 'Test Service')

class AppointmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(user=self.user, phone='1234567890')
        self.service = Service.objects.create(name='Test Service', duration=timedelta(hours=1), price=100.00)
        self.appointment = Appointment.objects.create(
            customer=self.customer,
            service=self.service,
            date_time=datetime.now() + timedelta(days=1),
            status='scheduled'
        )

    def test_appointment_creation(self):
        self.assertTrue(isinstance(self.appointment, Appointment))
        self.assertEqual(self.appointment.__str__(), f"{self.customer.user.username} - {self.service.name}")

class AppointmentFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.customer = Customer.objects.create(user=self.user, phone='1234567890')
        self.service = Service.objects.create(name='Test Service', duration=timedelta(hours=1), price=100.00)

    def test_appointment_form_valid(self):
        form_data = {
            'customer': self.customer.id,
            'service': self.service.id,
            'date_time': datetime.now() + timedelta(days=1),
            'notes': 'Test notes'
        }
        form = AppointmentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_appointment_form_invalid(self):
        form_data = {
            'customer': self.customer.id,
            'service': self.service.id,
            'date_time