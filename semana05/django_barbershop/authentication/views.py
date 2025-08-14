from rest_framework import generics, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError
from .models import RoleModel, UserModel
from .serializers import (
    RoleSerializer,
    RegisterSerializer,
    LoginSerializer,
)

@extend_schema(
    methods=['GET'],
    tags=['Roles'],
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
    tags=['Roles'],
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

@extend_schema(
    methods=['GET'],
    tags=['Roles'],
    responses={
        200: OpenApiResponse(
            description='Role by id',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Role by id',
                    value={
                        'ok': True,
                        'object': 'retrieve_role',
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
@extend_schema(
    methods=['PUT', 'PATCH'],
    tags=['Roles'],
    responses={
        200: OpenApiResponse(
            description='Role updated',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Role updated',
                    value={
                        'ok': True,
                        'object': 'update_role',
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
@extend_schema(
    methods=['DELETE'],
    tags=['Roles'],
    responses={
        200: OpenApiResponse(
            description='Role deleted',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Role deleted',
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
class RoleByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super().retrieve(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'retrieve_role',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'retrieve_role',
                    'error': 'Role not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'update_role',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'update_role',
                    'error': 'Role not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return Response(
                data={
                    'ok': True,
                    'object': 'delete_role',
                    'data': None
                },
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                data={
                    'ok': False,
                    'object': 'delete_role',
                    'error': 'Role not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )

@extend_schema(
    methods=['POST'],
    tags=['Auth'],
    responses={
        200: OpenApiResponse(
            description='User created',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='User created',
                    value={
                        'ok': True,
                        'object': 'register_user',
                        'data': {
                            'id': 1,
                            'name': 'John Doe',
                            'email': 'john@doe.com',
                            'status': True,
                            'role': 1
                        }
                    }
                )
            ]
        )
    }
)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'register_user',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )

@extend_schema(
    methods=['POST'],
    tags=['Auth'],
    responses={
        200: OpenApiResponse(
            description='User login',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='User login',
                    value={
                        'ok': True,
                        'object': 'login_user',
                        'data': {
                            'access': '',
                            'refresh': '',
                        }
                    }
                )
            ]
        )
    }
)
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            response = super().post(request)
            return Response(
                data={
                    'ok': True,
                    'object': 'login_user',
                    'data': response.data
                },
                status=status.HTTP_200_OK
            )
        except ValidationError:
            return Response(
                data={
                    'ok': False,
                    'object': 'login_user',
                    'error': 'Invalid credentials'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )