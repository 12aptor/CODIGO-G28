from django.db import models

class CustomerModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    document_number = models.CharField(max_length=8)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'customers'

class AppointmentModel(models.Model):
    date = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'authentication.UserModel',
        on_delete=models.CASCADE,
        related_name='appointments',
        db_column='user_id'
    )
    barber = models.ForeignKey(
        'services.BarberModel',
        on_delete=models.CASCADE,
        related_name='appointments',
        db_column='barber_id'
    )
    customer = models.ForeignKey(
        'CustomerModel',
        on_delete=models.CASCADE,
        related_name='appointments',
        db_column='customer_id'
    )
    service = models.ForeignKey(
        'services.ServiceModel',
        on_delete=models.CASCADE,
        related_name='appointments',
        db_column='service_id'
    )

    def __str__(self):
        return self.date
    
    class Meta:
        db_table = 'appointments'

class PaymentModel(models.Model):
    amount = models.FloatField()

    PAYMENT_METHOD = (
        ('CASH', 'CASH'),
        ('CREDIT_CARD', 'CREDIT_CARD'),
    )

    method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    created_at = models.DateTimeField(auto_now_add=True)
    appointment = models.ForeignKey(
        'AppointmentModel',
        on_delete=models.CASCADE,
        related_name='payments',
        db_column='appointment_id'
    )

    def __str__(self):
        return self.amount
    
    class Meta:
        db_table = 'payments'