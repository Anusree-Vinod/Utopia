from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="Category_images",null=True,blank=True)

class ProductDb(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to="Product_image", null=True, blank=True)