
from rest_framework import viewsets
from .models import CustomService, CustomAppointment
from .serializers import CustomAppointmentSerializer, CustomServiceSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import CustomAppointment, CustomService
from django.contrib.auth.models import User

class CustomServiceViewSet(viewsets.ModelViewSet):
    queryset = CustomService.objects.all()
    serializer_class = CustomServiceSerializer

class CustomAppointmentViewSet(viewsets.ModelViewSet):
    queryset = CustomAppointment.objects.all()
    serializer_class = CustomAppointmentSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id is not None:
            queryset = queryset.filter(customer__id=customer_id)
        return queryset