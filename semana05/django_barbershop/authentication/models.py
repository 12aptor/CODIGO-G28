from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class RoleModel(models.Model):
    ROLE_NAME = (
        ('ADMIN', 'ADMIN'),
        ('MANAGER', 'MANAGER'),
    )

    name = models.CharField(max_length=10, choices=ROLE_NAME, default='MANAGER')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'roles'


class UserModel(AbstractBaseUser):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.ForeignKey(
        'RoleModel',
        on_delete=models.CASCADE,
        related_name='users',
        db_column='role_id'
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'