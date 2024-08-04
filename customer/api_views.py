
# views.py
from rest_framework import generics
from .models import Customer
from .serializers import ClientSerializer

class ClientListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = ClientSerializer

