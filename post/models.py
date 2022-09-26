from django.db import models


class ArticleModel(models.Model):
    author_name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='media', verbose_name='Image')
    status = models.BooleanField(default=False)
    created_at = models.DateField()
    updated_at = models.DateField()


    def __str__(self):
        return self.title


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title