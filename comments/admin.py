from django.contrib import admin
from comments.models import CommentsModel


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('full_name','comments','created_at')
    search_fields = ['full_name','comments']
    list_per_page = 25 # No of records per page
admin.site.register(CommentsModel,CommentsAdmin)
