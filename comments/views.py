from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from comments.models import CommentsModel
from comments.serializers import CommentSerializers

class ListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializers
    queryset = CommentsModel.objects.all()


class RetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = CommentSerializers
    queryset = CommentsModel.objects.all()
