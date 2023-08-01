from django.db.models import Q
from django.contrib.auth.models import User
import json
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import UserSerializer
from .permissions import AnonPermissionOnly


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AnonPermissionOnly]


class AuthAPIView(APIView):
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'message': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username') # username or email address
        password = data.get('password')
        qs = User.objects.filter(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                return Response("")

        return Response({'detail': 'Invalid credentials'}, status=401)
