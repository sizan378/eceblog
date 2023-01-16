from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'first_name',
                    'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": ("email", "password")
            },
        ),
        (
            _("Personal Information"),
            {
                "fields":("city", "first_name", "last_name")
            },
        ),
        (
            _("Permissions and Group"),
            {
                "fields":("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
        (
            _("Important Dates"),
            {
                "fields":("last_login", "date_joined")
            },
        ),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('-id',)


admin.site.register(CustomUser, CustomUserAdmin)
