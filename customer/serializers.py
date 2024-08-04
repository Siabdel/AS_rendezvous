
# serializers.py
from rest_framework import serializers
from customer.models import Customer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'company', 'get_absolute_url']

        
    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url

