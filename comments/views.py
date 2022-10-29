

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from comments.models import CommentsModel
from comments.serializers import CommentSerializers


class CommentsListView(ListCreateAPIView):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentSerializers


class CommentsRetrieveView(RetrieveUpdateAPIView):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentSerializers

    # serializer = CommentSerializers(queryset, many=True)
