from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from comments.models import CommentsModel
from comments.serializers import CommentSerializers

class CommentListView(ListCreateAPIView):
    serializer_class = CommentSerializers
    queryset = CommentsModel.objects.all()


class CommentUpdateView(RetrieveUpdateAPIView):
    serializer_class = CommentSerializers
    queryset = CommentsModel.objects.all()
