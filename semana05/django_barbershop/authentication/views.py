from rest_framework import generics, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from .models import RoleModel
from .serializers import RoleSerializer

@extend_schema(
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description='List of roles',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='List roles',
                    value={
                        'ok': True,
                        'object': 'list_roles',
                        'data': [
                            {
                                'id': 1,
                                'name': 'ADMIN'
                            }
                        ]
                    },
                    response_only=True
                )
            ]
        )
    }
)
@extend_schema(
    methods=['POST'],
    responses={
        200: OpenApiResponse(
            description='Role created',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Role created',
                    value={
                        'ok': True,
                        'object': 'create_role',
                        'data': {
                            'id': 1,
                            'name': 'ADMIN'
                        }
                    }
                )
            ]
        )
    }
)
class RoleView(generics.ListCreateAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'list_roles',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            data={
                'ok':True,
                'object': 'create_role',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )
