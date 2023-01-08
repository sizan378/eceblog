from rest_framework.serializers import ModelSerializer

from .models import ArticleModel, CategoryModel


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ('id', 'author_name', 'title', 'body', 'category', 'image',
                  'status', 'created_at', 'updated_at')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'title')
