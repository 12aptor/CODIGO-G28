from django.urls import path
from .views import (
    index,
    date,
    json,
    product
)

urlpatterns = [
    path('inicio', index),
    path('fecha', date),
    path('json', json),
    path('producto/<int:id>', product),
]