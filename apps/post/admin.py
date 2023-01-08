from django.contrib import admin
from .models import ArticleModel, CategoryModel


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'title', 'category',
                    'status', 'created_at', 'updated_at')
    search_fields = ['title', 'author_name']
    list_per_page = 25  # No of records per page


admin.site.register(ArticleModel, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title']


admin.site.register(CategoryModel, CategoryAdmin)
