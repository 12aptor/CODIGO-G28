from django.urls import path
from .views import (
    AppointmentView,
    AppointmentPaymentView,
)

urlpatterns = [
    path('appointments/', AppointmentView.as_view()),
    path('appointments/<int:appointment_id>/payments/', AppointmentPaymentView.as_view()),
]