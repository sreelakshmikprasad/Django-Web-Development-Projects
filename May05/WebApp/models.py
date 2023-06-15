from django.db import models

# Create your models here.
class UserDB(models.Model):
    Uname=models.CharField(max_length=50,null=True,blank=True)
    UEmail=models.CharField(max_length=50,null=True,blank=True)
    UPhone=models.CharField(max_length=50,null=True,blank=True)
    UPassword=models.CharField(max_length=50,null=True,blank=True)
    UImage=models.ImageField(upload_to="User_Profile",null=True,blank=True)

class CartDB(models.Model):
    Uname=models.CharField(max_length=50,null=True,blank=True)
    Product=models.CharField(max_length=50,null=True,blank=True)
    PDescription=models.CharField(max_length=50,null=True,blank=True)
    Quantity=models.CharField(max_length=50,null=True,blank=True)
    Price=models.CharField(max_length=50,null=True,blank=True)
    Product_Image=models.ImageField(upload_to="Product_In_Cart",null=True,blank=True)