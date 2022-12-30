

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import CommentsModel
from .serializers import CommentSerializers


class CommentListView(ListCreateAPIView):
    serializer_class = CommentSerializers
    queryset = CommentsModel.objects.all()



class CommentUpdateView(RetrieveUpdateAPIView):
    
    serializer_class = CommentSerializers
    queryset = CommentsModel.objects.all()

    # serializer = CommentSerializers(queryset, many=True)
