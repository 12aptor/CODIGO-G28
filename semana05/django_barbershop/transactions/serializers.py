from rest_framework import serializers
from .models import AppointmentModel, CustomerModel

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = AppointmentModel
        fields = '__all__'

    def create(self, validated_data):
        customer = validated_data.pop('customer')

        customer, _ = CustomerModel.objects.get_or_create(
            email=customer.get('email'),
            document_number=customer.get('document_number'),
            defaults=customer
        )

        appointment = AppointmentModel.objects.create(
            customer=customer,
            **validated_data
        )

        return appointment
