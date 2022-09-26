from rest_framework.serializers import ModelSerializer

from post.models import ArticleModel, CategoryModel


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ('id','title','body','status','created_at','updated_at')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id','title')