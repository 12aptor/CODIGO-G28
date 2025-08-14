from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .models import ServiceModel, BarberModel, ScheduleModel
from .serializers import (
    ServiceSerializer,
    BarberSerializer,
    ScheduleSerializer
)
from authentication.permissions import IsAdmin
from django.http import Http404
from datetime import time

@extend_schema(
    methods=['GET'],
    tags=['Services'],
    responses={
        200: OpenApiResponse(
            description='List of services',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='List services',
                    value={
                        'ok': True,
                        'object': 'list_services',
                        'data': [
                            {
                                'id': 1,
                                'name': 'Barber',
                                'description': 'Barber service',
                                'price': 50.00,
                                'duration': 2
                            }
                        ]
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['POST'],
    tags=['Services'],
    responses={
        200: OpenApiResponse(
            description='Service created',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Service created',
                    value={
                        'ok': True,
                        'object': 'create_service',
                        'data': {
                            'id': 1,
                            'name': 'Barber',
                            'description': 'Barber service',
                            'price': 50.00,
                            'duration': 2
                        }
                    }
                )
            ]
        )
    }
)
class ServiceView(generics.ListCreateAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'create_service',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'list_services',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )
    
@extend_schema(
    methods=['GET'],
    tags=['Services'],
    responses={
        200: OpenApiResponse(
            description='Service by id',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Service by id',
                    value={
                        'ok': True,
                        'object': 'retrieve_service',
                        'data': {
                            'id': 1,
                            'name': 'Corte de cabello',
                            'description': 'Descripción de corte de cabello',
                            'price': 100.00,
                            'duration': 2
                        }
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['PUT', 'PATCH'],
    tags=['Services'],
    responses={
        200: OpenApiResponse(
            description='Service updated',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Service updated',
                    value={
                        'ok': True,
                        'object': 'update_service',
                        'data': {
                            'id': 1,
                            'name': 'Corte de cabello',
                            'description': 'Descripción de corte de cabello',
                            'price': 100.00,
                            'duration': 2
                        }
                    }
                )
            ]
        )
    }
)
class ServiceByIdView(generics.RetrieveUpdateAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'retrieve_service',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'retrieve_service',
                    'error': 'Service not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'update_service',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'update_service',
                    'error': 'Service not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

@extend_schema(
    methods=['GET'],
    tags=['Barbers'],
    responses={
        200: OpenApiResponse(
            description='List of barbers',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='List barbers',
                    value={
                        'ok': True,
                        'object': 'list_barbers',
                        'data': [
                            {
                                'id': 1,
                                'name': 'John Doe',
                                'email': 'john@gmail.com',
                                'phone': '987654321',
                                'speciality': 'Barber',
                                'status': True
                            }
                        ]
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['POST'],
    tags=['Barbers'],
    responses={
        200: OpenApiResponse(
            description='Barber created',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Barber created',
                    value={
                        'ok': True,
                        'object': 'create_barber',
                        'data': {
                            'id': 1,
                            'name': 'John Doe',
                            'email': 'john@gmail.com',
                            'phone': '987654321',
                            'speciality': 'Barber',
                            'status': True
                        }
                    }
                )
            ]
        )
    }
)    
class BarberView(generics.ListCreateAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'list_barbers',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'create_barber',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )

@extend_schema(
    methods=['GET'],
    tags=['Barbers'],
    responses={
        200: OpenApiResponse(
            description='Barber by id',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Barber by id',
                    value={
                        'ok': True,
                        'object': 'retrieve_barber',
                        'data': {
                            'id': 1,
                            'name': 'John Doe',
                            'email': 'john@gmail.com',
                            'phone': '987654321',
                            'speciality': 'Barber',
                            'status': True
                        }
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['PUT', 'PATCH'],
    tags=['Barbers'],
    responses={
        200: OpenApiResponse(
            description='Barber updated',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Barber updated',
                    value={
                        'ok': True,
                        'object': 'update_barber',
                        'data': {
                            'id': 1,
                            'name': 'John Doe',
                            'email': 'john@gmail.com',
                            'phone': '987654321',
                            'speciality': 'Barber',
                            'status': True
                        }
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['DELETE'],
    tags=['Barbers'],
    responses={
        200: OpenApiResponse(
            description='Barber deleted',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Barber deleted',
                    value={
                        'ok': True,
                        'object': 'delete_role',
                        'data': None
                    }
                )
            ]
        )
    }
)
class BarberByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'retrieve_barber',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'retrieve_barber',
                    'error': 'Barber not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'update_barber',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'update_barber',
                    'error': 'Barber not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )   

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.status = False
            instance.save()

            return Response(
                data={
                    'ok': True,
                    'object': 'delete_barber',
                    'data': None
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'delete_barber',
                    'error': 'Barber not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
        

@extend_schema(
    methods=['GET'],
    tags=['Schedules'],
    responses={
        200: OpenApiResponse(
            description='List of schedules',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='List schedules',
                    value={
                        'ok': True,
                        'object': 'list_schedules',
                        'data': [
                            {
                                'day_of_week': 'MONDAY',
                                'start_time': '08:00',
                                'end_time': '12:00',
                                'barber': 1,
                            }
                        ]
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['POST'],
    tags=['Schedules'],
    responses={
        200: OpenApiResponse(
            description='Schedule created',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Schedule created',
                    value={
                        'ok': True,
                        'object': 'create_schedule',
                        'data': {
                            'day_of_week': 'MONDAY',
                            'start_time': '08:00',
                            'end_time': '12:00',
                            'barber': 1,
                        }
                    }
                )
            ]
        )
    }
)
class ScheduleView(generics.ListCreateAPIView):
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'list_schedules',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'create_schedule',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )

@extend_schema(
    methods=['GET'],
    tags=['Schedules'],
    responses={
        200: OpenApiResponse(
            description='Schedule by id',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Schedule by id',
                    value={
                        'ok': True,
                        'object': 'retrieve_schedule',
                        'data': {
                            'id': 1,
                            'day_of_week': 'MONDAY',
                            'start_time': '08:00',
                            'end_time': '12:00',
                            'barber': 1,
                        }
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['PUT', 'PATCH'],
    tags=['Schedules'],
    responses={
        200: OpenApiResponse(
            description='Schedule updated',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Schedule updated',
                    value={
                        'ok': True,
                        'object': 'update_schedule',
                        'data': {
                            'id': 1,
                            'day_of_week': 'MONDAY',
                            'start_time': '08:00',
                            'end_time': '12:00',
                            'barber': 1,
                        }
                    }
                )
            ]
        )
    }
)
@extend_schema(
    methods=['DELETE'],
    tags=['Schedules'],
    responses={
        200: OpenApiResponse(
            description='Schedule deleted',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Schedule deleted',
                    value={
                        'ok': True,
                        'object': 'delete_schedule',
                        'data': None
                    }
                )
            ]
        )
    }
)
class ScheduleByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'retrieve_schedule',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'retrieve_schedule',
                    'error': 'Schedule not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'update_schedule',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'update_schedule',
                    'error': 'Schedule not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'delete_schedule',
                    'data': None
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'delete_schedule',
                    'error': 'Schedule not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


@extend_schema(
    methods=['GET'],
    tags=['Barbers'],
    responses={
        200: OpenApiResponse(
            description='List of available barbers',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='List available barbers',
                    value={
                        'ok': True,
                        'object': 'list_barbers_available',
                        'data': [
                            {
                                'id': 1,
                                'name': 'John Doe',
                                'email': 'john@gmail.com',
                                'phone': '987654321',
                                'speciality': 'Barber',
                                'status': True
                            }
                        ]
                    }
                )
            ]
        )
    }
)
class BarberAvailableView(generics.ListAPIView):
    queryset = BarberModel.objects.all()
    serializer_class = BarberSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        day = self.kwargs.get('day') # MONDAY, TUESDAY
        start_time = self.kwargs.get('start_time') # 08:00
        end_time = self.kwargs.get('end_time') # 12:00
        print(day, start_time, end_time)

        return self.queryset.filter(
            schedules__day_of_week=day,
            schedules__start_time__lte=time.fromisoformat(start_time),
            schedules__end_time__gte=time.fromisoformat(end_time)
        ).distinct()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'list_barbers_available',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )