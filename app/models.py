from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):

    email      = models.CharField(max_length=100, help_text="correo@dom.com",unique=True)
    phone_number = models.CharField(max_length=50, help_text="3323232",  null=True)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)