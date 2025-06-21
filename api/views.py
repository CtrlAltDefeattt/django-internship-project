from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

# Create your views here.

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class RegisterView(generics.CreateAPIView):
    """
    Handles user registration.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class PublicApiView(APIView):
    """
    A public endpoint that requires no authentication.
    """
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"message": "This is a public endpoint."})

class ProtectedApiView(APIView):
    """
    A protected endpoint that requires JWT authentication.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}! This is a protected endpoint."})
