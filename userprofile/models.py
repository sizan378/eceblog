import email
from django.db import models



class UserProfileModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100)
    religion = models.CharField(max_length=100, null=True, blank=True)
