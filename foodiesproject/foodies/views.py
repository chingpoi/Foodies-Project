from django.shortcuts import redirect, render
from django.db import transaction
from django.views.generic import View
from .forms import *
from django.http import HttpResponse

# Create your views here.
class IndexView(View):
	def get(self,request):
		return render(request,'index.html')

class AboutView(View):
	def get(self,request):
		return render(request,'about.html')

class FeaturesView(View):
	def get(self,request):
		return render(request,'features.html')

class ContactView(View):
	def get(self,request):
		return render(request,'contact.html')

class LoginView(View):
	def get(self,request):
		return render(request,'login.html')

class RegisterView(View):
	def get(self,request):
		user = User.objects.all()
		address = Address.objects.all()
		context = {
			'user': user,
			'address': address
		}
		return render(request,'registration.html', context)

class DashboardView(View):
	def get(self,request):
		restaurants = Restaurant.objects.all()
		resDesc = Restaurant.objects.values('Restaurant_Desc').distinct()
		
		countAmerican = Restaurant.objects.filter(Restaurant_Desc = 'American').count()
		countAsian = Restaurant.objects.filter(Restaurant_Desc = 'Asian').count()
		countCoffee = Restaurant.objects.filter(Restaurant_Desc = 'Coffee').count()
		countFilipino = Restaurant.objects.filter(Restaurant_Desc = 'Filipino').count()
		countCouple = Restaurant.objects.filter(Restaurant_Desc = 'Couple').count()
		addStreet = Address.objects.values('Address_City').distinct()
		countCebu = Address.objects.filter(Address_City = 'Cebu').count()
		countMandaue = Address.objects.filter(Address_City = 'Mandaue').count()
		user = User.objects.all()
		address = Address.objects.all()
		context = {
			'user': user,
			'address': address,
			'restaurants': restaurants,
			'countAmerican': countAmerican,
			'countAsian': countAsian,
			'countCoffee': countCoffee,
			'countFilipino': countFilipino,
			'countCouple': countCouple,
			'resDesc': resDesc,
			'addStreet': addStreet,
			'countCebu': countCebu,
			'countMandaue': countMandaue 
		}
		return render(request,'dashboard.html', context)

	def get(self,request):
		user = User.objects.all()
		restaurants = Restaurant.objects.all()
		address = Address.objects.all()
		food = Food.objects.all()
		driver = Driver.objects.all()
		order = Order.objects.all()
		orderItem = OrderItem.objects.all()
		context = {
			'user': user,
			'restaurants': restaurants,
			'address': address,
			'food': food,
			'driver': driver,
			'order': order,
			'orderItem': orderItem,
		}
		return render(request,'dashboard.html', context)

	def AddUser(request):
		if request.method == "POST":
			form = UserForm(request.POST)
			
			if form.is_valid():
				print(form.is_valid())
				#FOREIGN USER ATTRIBUTES
				uAddressProvince = request.POST.get("userAddressProvince")
				uAddressCity = request.POST.get("userAddressCity")
				uAddressStreet = request.POST.get("userAddressStreet")

				#PRIMARY USER ATTRIBUTES
				uFname = request.POST.get("userFirstname")
				uLname = request.POST.get("userLastname")
				uPassword = request.POST.get("userPassword")
				uContactNumber = request.POST.get("usercontactNumber")
				uEmail = request.POST.get("userEmail")

				
				aForm = Address(Address_province = uAddressProvince, Address_City = uAddressCity, Address_Street = uAddressStreet)
				aForm.save()
				uAddressID = Address.objects.get(Address_ID = "1")
				form = User(User_FirstName = uFname, User_LastName = uLname, User_Password = uPassword, User_ContactNumber = uContactNumber, User_Email = uEmail, Address_ID = uAddressID)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')




#CHING'S CODES

def DeleteUser(request, id):  
    user = User.objects.get(User_ID=id)  
    user.delete()  
    return redirect('http://127.0.0.1:8000/dashboard/')  

def UpdateUser(request, id):  
    user = User.objects.get(User_ID=id)  
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect('http://127.0.0.1:8000/dashboard/')  
    return render(request, 'http://127.0.0.1:8000/dashboard/', {'user': user})

class RestaurantRegisterView(View):
	def get(self,request):
		return render(request, 'resRegister.html')

	def AddRestaurant(request):
		if request.method == "POST":
			form = RestaurantForm(request.POST)
			if form.is_valid():
				print(form.is_valid())
				rName = request.POST.get("Restaurant_Name")
				rDesc = request.POST.get("Restaurant_Desc")
				rContact = request.POST.get("Restaurant_ContactNumber")
				bAddress = request.POST.get("Address_ID")
				rAddress = Address.objects.get(Address_ID = bAddress)

				form = Restaurant(Restaurant_Name = rName, Restaurant_Desc = rDesc, Restaurant_ContactNumber = rContact, Address_ID = rAddress)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')
				