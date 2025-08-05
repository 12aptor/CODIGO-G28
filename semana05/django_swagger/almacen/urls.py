from django.urls import path
from .views import (
    CategoryView,
    CategoryByIdView,
)

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', CategoryByIdView.as_view())
]