from django.contrib import admin
from .models import ArticleModle


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','status','created_at','updated_at')
admin.site.register(ArticleModle,ArticleAdmin)
