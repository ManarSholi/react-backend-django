from rest_framework import serializers
from customers.models import Customer


class CustomerSelializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
