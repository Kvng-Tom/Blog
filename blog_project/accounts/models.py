from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from django.utils import timezone



# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('app_admin', 'App Admin'),
        ('root_admin', 'Root Admin'),
        ('super_admin', 'Super Admin'),
        ('user', 'User'),


    )

    full_name = models.CharField(max_length=250)
    role = models.CharField(max_length = 225, choices=ROLE_CHOICES)
    email = models.CharField(max_length=300,unique=True) #null=True, blank=True)
   
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = UserManager()


class OTP(models.Model):
        
        otp = models.CharField(max_length=6)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        expiry_date = models.DateTimeField()


        def is_otp_valid(self):

            return bool(self.expiry_date > timezone.now())


   