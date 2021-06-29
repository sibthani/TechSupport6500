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
    staff_code = models.ForeignKey("Staff", on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=6,null=True)
    cluster_code = models.ForeignKey("Cluster", on_delete=models.CASCADE, null=True)
    center_code = models.ForeignKey("Center", on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=254)
    phone_number = models.IntegerField(null=True)
    registration_date = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.username}"


"""
The cluster define a defined work portion which has locations called Centers
The model below defines that
"""

class Cluster(models.Model):
    cluster_code = models.CharField(max_length = 3, primary_key=True)
    cluster_name = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cluster_code}"

# Center is a subset of a cluster, FK in the model is PK in Cluster model
class Center(models.Model):
    cluster_code = models.ForeignKey("Cluster", on_delete=models.CASCADE)
    center_code = models.CharField(max_length=3, primary_key=True)
    center_name = models.CharField(max_length=50)
    center_address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.center_code}"


"""
Defines Staff credentials and other issues that pertain to particular staff
"""
class Staff(models.Model):
    staff_code = models.CharField(max_length=3, primary_key=True)
    career_descrptn = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.staff_code}"


class Issue_Catgry(models.Model):
    issue_code = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=150)


    def __str__(self):
        return f"{self.issue_code}"


# Issues are defined by codes LPTOP - Laptop issues
class Issue(models.Model):
    issue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    issue_code = models.ForeignKey("Issue_Catgry", on_delete=models.CASCADE)
    username = models.ForeignKey("CoachUser", on_delete=models.CASCADE)
    cluster_code = models.ForeignKey("Cluster", on_delete=models.CASCADE, null=True)
    center_code = models.ForeignKey("Center", on_delete=models.CASCADE, null=True)
    issue_description = models.TextField(max_length=150)
    urgent = models.CharField(max_length=10)
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.issue_id}"

    
