
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import CustomAppointment, CustomService, StaffMember, Availability, Conflict
from .models import  Customer
from .serializers import StaffMemberSerializer, AvailabilitySerializer, ConflictSerializer
from .serializers import CustomAppointmentSerializer, CustomServiceSerializer, UserSerializer, CustomerSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class CustomServiceViewSet(viewsets.ModelViewSet):
    queryset = CustomService.objects.all()
    serializer_class = CustomServiceSerializer
    permission_classes = [IsAuthenticated]

class CustomAppointmentViewSet(viewsets.ModelViewSet):
    queryset = CustomAppointment.objects.all()
    serializer_class = CustomAppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CustomAppointment.objects.all()
        client_id = self.request.query_params.get('client_id', None)
        if client_id is not None:
            queryset = queryset.filter(client__id=client_id)
        return queryset
    
class StaffMemberViewSet(viewsets.ModelViewSet):
    queryset = StaffMember.objects.all()
    serializer_class = StaffMemberSerializer
    permission_classes = [IsAuthenticated]

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]

class ConflictViewSet(viewsets.ModelViewSet):
    queryset = Conflict.objects.all()
    serializer_class = ConflictSerializer
    permission_classes = [IsAuthenticated]