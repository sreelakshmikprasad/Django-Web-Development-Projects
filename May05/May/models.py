from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Category=models.CharField(max_length=50,null=True,blank=True)
    Category_Image=models.ImageField(upload_to="Category_Img",null=True,blank=True)
    Description=models.TextField(max_length=50,null=True,blank=True)

class ProductDB(models.Model):
    Category=models.CharField(max_length=50,null=True,blank=True)
    Product=models.CharField(max_length=50,null=True,blank=True)
    Price=models.CharField(max_length=50,null=True,blank=True)
    PDescription=models.TextField(max_length=50,null=True,blank=True)
    Brand=models.CharField(max_length=50,null=True,blank=True)
    Product_Image=models.ImageField(upload_to="Product_Img",null=True,blank=True)


class ContactsDB(models.Model):
    CName=models.CharField(max_length=50,null=True,blank=True)
    CEmail=models.CharField(max_length=50,null=True,blank=True)
    CSubject=models.CharField(max_length=50,null=True,blank=True)
    CMessage=models.CharField(max_length=50,null=True,blank=True)

class OrderDB(models.Model):
    FName=models.CharField(max_length=50,null=True,blank=True)
    LName=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Phone=models.CharField(max_length=50,null=True,blank=True)
    AddrsLine1=models.CharField(max_length=50,null=True,blank=True)
    AddrsLine2=models.CharField(max_length=50,null=True,blank=True)
    Country=models.CharField(max_length=50,null=True,blank=True)
    City=models.CharField(max_length=50,null=True,blank=True)
    State=models.CharField(max_length=50,null=True,blank=True)
    PinCode=models.IntegerField(null=True,blank=True)