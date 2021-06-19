from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

import uuid

# Create your models here.
class CoachUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=12, primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    #coach_career = models.ForeignKey("careerconfig", on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=6,null=True)
    #country_code = models.ForeignKey("countryconfig", on_delete=models.CASCADE,null=True)
    #cluster_code = models.ForeignKey("clusterconfig", on_delete=models.CASCADE, null=True)
    #center_code = models.ForeignKey("centerconfig", on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=254)
    mobile_money = models.IntegerField(null=True)
    registration_date = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.username}"