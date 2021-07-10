from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=40, unique=True)
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    description = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="tag_product")
    price = models.IntegerField()
    product_code = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    image = models.ImageField(upload_to="my_image", blank=True)
    create_at = models.DateField(auto_now=False, auto_now_add=True)
    update_at = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.description


