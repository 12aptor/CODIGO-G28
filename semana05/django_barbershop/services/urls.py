from django.urls import path
from .views import (
    ServiceView,
    ServiceByIdView,
)

urlpatterns = [
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>/', ServiceByIdView.as_view()),
]