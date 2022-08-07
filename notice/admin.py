from django.contrib import admin
from .models import NoticeModel


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','notice')
admin.site.register(NoticeModel, NoticeAdmin)
