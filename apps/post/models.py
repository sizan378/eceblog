from django.db import models
from apps.comments.models import CommentsModel


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ArticleModel(models.Model):
    author_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='image', verbose_name='Image')
    category = models.ForeignKey(CategoryModel, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    # comment = models.ForeignKey(CommentsModel, on_delete=models.DO_NOTHING)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title
