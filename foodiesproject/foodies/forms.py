from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

class RegisterForm(forms.Form):
    User_FirstName = models.CharField(max_length = 50)
    User_LastName = models.CharField(max_length = 50)
    User_Password = models.CharField(max_length = 50)
    User_ContactNumber = models.CharField(max_length = 50)
    User_Email = models.EmailField(max_length = 50, unique = True)
    Address_Province = models.CharField(max_length = 50)
    Address_City = models.CharField(max_length = 50)
    Address_Street = models.CharField(max_length = 50)