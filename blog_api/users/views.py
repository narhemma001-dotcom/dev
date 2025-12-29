from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]  