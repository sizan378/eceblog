import imp
from django.shortcuts import render
from .models import NoticeModel
from .serializer import NoticeSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from apps.post.pagination import CustomNumberPagination
# from rest_framework import authentication, IsA

class NoticeListView(GenericAPIView):
    
    queryset = NoticeModel.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = CustomNumberPagination

    def get(self, request, format=None):
        notice = NoticeModel.objects.all()
        serializer = NoticeSerializer(notice, many=True)
        return Response(serializer.data)

    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = NoticeModel.objects.all()
    serializer_class = NoticeSerializer

    permission_classes = (IsAdminUser, IsAuthenticated, )

    def post(self, request, format=None):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeDetailView(GenericAPIView):
   
    queryset = NoticeModel.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return NoticeModel.objects.get(pk=pk)
        except NoticeModel.DoesNotExist:
            raise Http404


    
    def get(self, request, pk, format=None):
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)


    permission_classes = (IsAdminUser, IsAuthenticated)

    def put(self, request, pk, format=None):
        
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
