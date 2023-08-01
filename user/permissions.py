from rest_framework import permissions

from django.contrib.auth.models import User

class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticated'

    def has_permission(self, request, view):
        return not request.user.is_authenticated