

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from comments.models import CommentsModel
from comments.serializers import CommentSerializers

<<<<<<< HEAD

class CommentsListView(ListCreateAPIView):
=======
class CommentListView(ListCreateAPIView):
    serializer_class = CommentSerializers
>>>>>>> c638cfd2ee87711ba98f489361583b664058678b
    queryset = CommentsModel.objects.all()
    serializer_class = CommentSerializers


<<<<<<< HEAD
class CommentsRetrieveView(RetrieveUpdateAPIView):
=======
class CommentUpdateView(RetrieveUpdateAPIView):
    serializer_class = CommentSerializers
>>>>>>> c638cfd2ee87711ba98f489361583b664058678b
    queryset = CommentsModel.objects.all()
    serializer_class = CommentSerializers

    # serializer = CommentSerializers(queryset, many=True)
