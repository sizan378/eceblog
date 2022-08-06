from django.shortcuts import render
from rest_framework. views import APIView 
from .models import ArticleModle
from .serializer import ArticleSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

class ArticleListView(APIView):
    @swagger_auto_schema(responses={200: ArticleSerializer(many=True)})
    def get(self, request, format=None):
        article = ArticleModle.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="This is post method")
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):
   
    def get_object(self, pk):
        try:
            return ArticleModle.objects.get(pk=pk)
        except ArticleModle.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="This is get details ")
    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="This is put method")
    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
