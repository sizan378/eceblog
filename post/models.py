from django.db import models


class ArticleModle(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateField()
    updated_at = models.DateField()


    def __str__(self):
        return self.title