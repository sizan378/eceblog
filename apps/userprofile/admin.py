from django.contrib import admin
from .models import UserProfileModel


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','phone_number','country',"university",'department')
    search_fields = ['first_name','phone_number','university','department']
    list_per_page = 25 # No of records per page
admin.site.register(UserProfileModel, UserProfileAdmin)
