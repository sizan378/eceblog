from django.contrib import admin
from .models import UserProfileModel


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','phone_number','country',"university",'department')
admin.site.register(UserProfileModel, UserProfileAdmin)
