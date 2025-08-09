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

class ScheduleModel(models.Model):
    DAY_OF_WEEK = (
        ('MONDAY', 'MONDAY'),
        ('TUESDAY', 'TUESDAY'),
        ('WEDNESDAY', 'WEDNESDAY'),
        ('THURSDAY', 'THURSDAY'),
        ('FRIDAY', 'FRIDAY'),
        ('SATURDAY', 'SATURDAY'),
        ('SUNDAY', 'SUNDAY'),
    )

    day_of_week = models.CharField(max_length=10, choices=DAY_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    barber = models.ForeignKey(
        'BarberModel',
        on_delete=models.CASCADE,
        related_name='schedules',
        db_column='barber_id'
    )

    def __str__(self):
        return self.day_of_week
    
    class Meta:
        db_table = 'schedules'