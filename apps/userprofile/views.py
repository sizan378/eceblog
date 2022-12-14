import imp
from django.shortcuts import render
from .models import UserProfileModel
from .serializer import UserProfileSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView


class UserProfileListView(GenericAPIView):
    
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )
    def get(self, request, format=None):
        userprofile = UserProfileModel.objects.all()
        serializer = UserProfileSerializer(userprofile, many=True)
        return Response(serializer.data)

    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetailView(GenericAPIView):

    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer
    def get_object(self, pk):
        try:
            return UserProfileModel.objects.get(pk=pk)
        except UserProfileModel.DoesNotExist:
            raise Http404

    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )
    def get(self, request, pk, format=None):
        userprofile = self.get_object(pk)
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)

    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )
    def put(self, request, pk, format=None):
        userprofile = self.get_object(pk)
        serializer = UserProfileSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
