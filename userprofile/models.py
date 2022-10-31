from django.db import models
from django.core.validators import RegexValidator

class UserProfileModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^01[3-9]\d{8}$', message="Phone number must be entered in the format: '+8801*********'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    address = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100)
    religion = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.first_name