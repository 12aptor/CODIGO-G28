from django.urls import path
from .views import (
    RoleView,
    RoleByIdView,
    RegisterView,
    LoginView,
)

urlpatterns = [
    path('roles/', RoleView.as_view()),
    path('roles/<int:pk>/', RoleByIdView.as_view()),

    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', LoginView.as_view()),
]