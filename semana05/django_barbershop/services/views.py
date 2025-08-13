from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .models import ServiceModel
from .serializers import ServiceSerializer
from authentication.permissions import IsAdmin
from django.http import Http404

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
                    'object': 'retrieve_service',
                    'error': 'Service not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )