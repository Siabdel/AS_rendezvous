
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomAppointment, CustomService, Customer
from rest_framework import serializers
from .models import CustomAppointment, CustomService, StaffMember, Availability, Conflict

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone']

class CustomServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomService
        fields = ['id', 'name', 'description', 'duration', 'price']

class CustomAppointmentSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    service = CustomServiceSerializer(read_only=True)

    class Meta:
        model = CustomAppointment
        fields = ['id', 'client', 'service', 'phone', 'address', 'want_reminder', 'additional_info', 'paid', 'amount_to_pay', 'created_at', 'updated_at']

    def create(self, validated_data):
        client_id = self.context['request'].data.get('client_id')
        service_id = self.context['request'].data.get('service_id')
        client = User.objects.get(id=client_id)
        service = CustomService.objects.get(id=service_id)
        return CustomAppointment.objects.create(client=client, service=service, **validated_data)


class StaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = ['id', 'user', 'services']

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['id', 'staff_member', 'day_of_week', 'start_time', 'end_time']

class ConflictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conflict
        fields = ['id', 'staff_member', 'date', 'start_time', 'end_time', 'reason']