from django.urls import path
from .views import CategoryView, ProductView, ProductByIdView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductByIdView.as_view()),
]