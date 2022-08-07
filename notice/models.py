from django.db import models



class NoticeModel(models.Model):
    notice = models.TextField()

    def __str__(self):
        return self.notice
    
