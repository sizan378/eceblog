from django.db import models



class NoticeModel(models.Model):
    title = models.CharField(max_length=100)
    notice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notice
    
