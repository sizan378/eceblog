from rest_framework.serializers import ModelSerializer
from .models import CommentsModel


class CommentSerializers(ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = '__all__'