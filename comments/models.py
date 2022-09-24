from django.db import models


class CommentsModel(models.Model):
    full_name = models.CharField(max_length=200)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.full_name