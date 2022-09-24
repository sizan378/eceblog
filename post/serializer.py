from rest_framework.serializers import ModelSerializer
from .models import ArticleModel


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ('id','title','body','status','created_at','updated_at')