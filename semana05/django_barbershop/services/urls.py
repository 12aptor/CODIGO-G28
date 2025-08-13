from django.urls import path
from .views import (
    ServiceView,
    ServiceByIdView,
    BarberView,
    BarberByIdView,
)

urlpatterns = [
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>/', ServiceByIdView.as_view()),

    path('barbers/', BarberView.as_view()),
    path('barbers/<int:pk>/', BarberByIdView.as_view()),
]