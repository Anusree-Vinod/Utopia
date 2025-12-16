from django.db import models

# Create your models here.
class RegistrationDB(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email =  models.CharField(max_length=50,null=True,blank=True)
    contact =  models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    password =  models.CharField(max_length=50,null=True,blank=True)
    confirm_pwd =  models.CharField(max_length=50,null=True,blank=True)

class ContactDB(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

class cartDB(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True)
    product = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to="cart_images",null=True,blank=True)

class orderDB(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    contact = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    pincode = models.CharField(max_length=50,null=True,blank=True)
    total_amt = models.IntegerField(null=True,blank=True)