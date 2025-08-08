from django.db import models

class ServiceModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'services'

class BarberModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=9)
    speciality = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'barbers'