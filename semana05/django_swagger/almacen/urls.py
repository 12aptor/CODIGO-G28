from django.urls import path
from .views import (
    CategoryView,
    CategoryByIdView,
    ProductView,
    ProductByIdView,
)

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:pk>/', CategoryByIdView.as_view()),
    path('products/', ProductView.as_view()),
    path('products/<int:pk>/', ProductByIdView.as_view()),
]