from rest_framework.serializers import ModelSerializer
from .models import ArticleModle


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = ArticleModle
        fields = ('id','title','body','status','created_at','updated_at')