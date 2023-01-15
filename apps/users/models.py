from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manage import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), unique=True)
    first_name= models.CharField(_('First Name'), max_length=50, blank=True, null=True)
    last_name= models.CharField(_('Last Name'), max_length=50, blank=True, null=True)
    city = models.CharField(_('City'), max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(_('Last login'), default=timezone.now)
    date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email