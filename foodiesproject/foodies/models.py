from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Address(models.Model):
    Address_ID = models.AutoField(auto_created = True, primary_key = True)
    Address_Province = models.CharField(max_length = 50)
    Address_City = models.CharField(max_length = 50)
    Address_Street = models.CharField(max_length = 50)
    
    class meta:
        db_table = 'tblAddress'

class User(models.Model):
    User_ID = models.AutoField(auto_created = True, primary_key = True)
    User_FirstName = models.CharField(max_length = 50)
    User_LastName = models.CharField(max_length = 50)
    User_Password = models.CharField(max_length = 50)
    User_ContactNumber = models.CharField(max_length = 50)
    User_Email = models.EmailField(max_length = 50, unique = True)
    Address_ID = models.ForeignKey(Address, on_delete = models.CASCADE)
    
    class meta:
        db_table = 'tblUser'

class Restaurant(models.Model):
    Restaurant_ID = models.AutoField(auto_created = True, primary_key = True)
    Restaurant_Name = models.CharField(max_length = 50)
    Restaurant_Desc = models.CharField(max_length = 100)
    Restaurant_ContactNumber = models.CharField(max_length = 50)
    Address_ID = models.ForeignKey(Address, on_delete = models.CASCADE)

    class meta:
        db_table = 'tblRestaurant'

class Food(models.Model):
    Food_ID = models.AutoField(auto_created = True, primary_key = True)
    Restaurant_ID = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    Food_Name = models.CharField(max_length = 50)
    Food_Desc = models.CharField(max_length = 100)
    Food_Price = models.IntegerField()

    class meta:
        db_table = 'tblFood'

class Driver(models.Model):
    Driver_ID = models.AutoField(auto_created = True, primary_key = True)
    Driver_FirstName = models.CharField(max_length = 50)
    Driver_LastName = models.CharField(max_length = 50)
    Driver_Email = models.EmailField(max_length = 50)
    Address_ID = models.ForeignKey(Address, on_delete = models.CASCADE)
    Driver_ContactNumber = models.CharField(max_length = 50)

    class meta:
        db_table = 'tblDriver'

class Order(models.Model):
    Order_ID = models.AutoField(auto_created = True, primary_key = True)
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    Order_Type = models.CharField(max_length = 50)
    Driver_ID = models.ForeignKey(Driver, on_delete = models.CASCADE, null = True)
    Order_TotalCost = models.IntegerField()
    Date = models.CharField(max_length = 10)
    Time = models.CharField(max_length = 10)

    class meta:
        db_table = 'tblOrder'

class OrderItem(models.Model):
    OrderItem_ID = models.AutoField(auto_created = True, primary_key = True)
    Order_ID = models.ForeignKey(Order, on_delete = models.CASCADE)
    Food_ID = models.ForeignKey(Food, on_delete = models.CASCADE)
    Quantity = models.IntegerField()
    Cost = models.IntegerField()

    class meta:
        db_table = 'tblOrderItem'