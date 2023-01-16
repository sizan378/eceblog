from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import CustomUserSerializer, CustomUserLogin
from rest_framework_simplejwt.views import TokenObtainPairView


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistration(APIView):
    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"token": token})
        return Response(serializer.error_messages)

class UserLogin(APIView):
    def post(self, request, format=None):
        serializer = CustomUserLogin(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"token": token})
            else:
                return Response("please provide email and password")

# class UserRegistration(TokenObtainPairView):
#     '''For admin Get access token & refresh token
#     and update last_login'''
#     permission_classes = (AllowAny,)
#     serializer_class = CustomUserSerializer