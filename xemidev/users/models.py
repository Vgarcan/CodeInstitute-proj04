from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class User(AbstractUser):
    """"
    Custom user model extending Django's AbstractUser.
    Includes additional fields for storing user contact details and company details.

    """

    phone_number = models.CharField(max_length=20, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_address = models.CharField(max_length=250, null=True, blank=True)
    company_type = models.CharField(max_length=100, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="user_set_group",

    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="user_set_permissions",

    )
