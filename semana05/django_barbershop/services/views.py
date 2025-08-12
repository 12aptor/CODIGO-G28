from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .models import ServiceModel
from .serializers import ServiceSerializer

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
    permission_classes = [IsAuthenticated]

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