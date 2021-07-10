from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager


class myUser(AbstractUser):
    full_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="email", max_length=90, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['full_name', 'company_name', 'email']

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    id_user = models.OneToOneField(myUser, on_delete=models.CASCADE, primary_key=True)
    avatar = models.TextField(max_length=200)

