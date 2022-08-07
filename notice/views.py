import imp
from django.shortcuts import render
from .models import NoticeModel
from .serializer import NoticeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
# from rest_framework import authentication, IsA

class NoticeListView(GenericAPIView):
    
    serializer_class = NoticeSerializer
    def get(self, request, format=None):
        notice = NoticeModel.objects.all()
        serializer = NoticeSerializer(notice, many=True)
        return Response(serializer.data)

    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = NoticeSerializer
    def post(self, request, format=None):
        serializer = NoticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoticeDetailView(GenericAPIView):
   
    serializer_class = NoticeSerializer
    def get_object(self, pk):
        try:
            return NoticeModel.objects.get(pk=pk)
        except NoticeModel.DoesNotExist:
            raise Http404

    serializer_class = NoticeSerializer
    def get(self, request, pk, format=None):
        serializer_class = NoticeSerializer
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)

    serializer_class = NoticeSerializer
    def put(self, request, pk, format=None):
        serializer_class = NoticeSerializer
        notice = self.get_object(pk)
        serializer = NoticeSerializer(notice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
