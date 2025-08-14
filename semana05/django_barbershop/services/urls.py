from django.urls import path
from .views import (
    ServiceView,
    ServiceByIdView,
    BarberView,
    BarberByIdView,
    ScheduleView,
    ScheduleByIdView,
    BarberAvailableView,
)

urlpatterns = [
    path('services/', ServiceView.as_view()),
    path('services/<int:pk>/', ServiceByIdView.as_view()),

    path('barbers/', BarberView.as_view()),
    path('barbers/<int:pk>/', BarberByIdView.as_view()),
    path('barbers/available/<str:day>/<str:start_time>/<str:end_time>/', BarberAvailableView.as_view()),

    path('schedules/', ScheduleView.as_view()),
    path('schedules/<int:pk>/', ScheduleByIdView.as_view()),

]