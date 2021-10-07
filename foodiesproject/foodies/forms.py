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