from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # print(request.user.is_authenticated)
        # print(request.user.role.name)
        if request.user.role.name != 'ADMIN':
            raise AuthenticationFailed(
                detail={
                    'ok': False,
                    'object': 'authentication',
                    'error': 'You are not an admin'
                },
                code=status.HTTP_403_FORBIDDEN
            )
        return True
    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name != 'MANAGER':
            raise AuthenticationFailed(
                detail={
                    'ok': False,
                    'object': 'authentication',
                    'error': 'You are not an manager'
                },
                code=status.HTTP_403_FORBIDDEN
            )
        return True