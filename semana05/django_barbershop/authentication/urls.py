from django.urls import path
from .views import (
    RoleView,
    # CreateRoleView,
)

urlpatterns = [
    path('roles/', RoleView.as_view()),
    # path('roles/create', CreateRoleView.as_view()),
]