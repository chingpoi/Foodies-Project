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

	#FOR USER
	def AddUser(request):
		if request.method == "POST":
			form = UserForm(request.POST)
			
			if form.is_valid():
				print(form.is_valid())
				#FOREIGN USER ATTRIBUTES
				bAddress = request.POST.get("Address_ID")
				uAddress = Address.objects.get(Address_ID = bAddress)

				#PRIMARY USER ATTRIBUTES
				uFname = request.POST.get("User_FirstName")
				uLname = request.POST.get("User_LastName")
				uPassword = request.POST.get("User_Password")
				uContactNumber = request.POST.get("User_ContactNumber")
				uEmail = request.POST.get("User_Email")

				
				form = User(User_FirstName = uFname, User_LastName = uLname, User_Password = uPassword, User_ContactNumber = uContactNumber, User_Email = uEmail, Address_ID = uAddress)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')
		
	#FOR ADDRESS
	def AddAddress(request):
		if request.method == "POST":
			form = AddressForm(request.POST)

			if form.is_valid():
				print(form.is_valid())

				#PRIMARY ADDRESS ATTRIBUTES
				aProvince = request.POST.get("Address_Province")
				aCity = request.POST.get("Address_City")
				aStreet = request.POST.get("Address_Street")

				form = Address(Address_Province = aProvince, Address_City = aCity, Address_Street = aStreet)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR FOOD
	def AddFood(request):
		if request.method == "POST":
			form = FoodForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#FOREIGN RESTAURANT ATTRIBUTES
				bRestaurant = request.POST.get("Restaurant_ID")
				uRestaurant = Restaurant.objects.get(Restaurant_ID = bRestaurant)

				#PRIMARY FOOD ATTRIBUTES
				fName = request.POST.get("Food_Name")
				fDesc = request.POST.get("Food_Desc")
				fPrice = int(request.POST.get("Food_Price"))

				form = Food(Restaurant_ID = uRestaurant, Food_Name = fName, Food_Desc = fDesc, Food_Price = fPrice)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')


	#FOR DRIVER
	def AddDriver(request):
		if request.method == "POST":
			form = DriverForm(request.POST)
			
			if form.is_valid():
				print(form.is_valid())
				#FOREIGN DRIVER ATTRIBUTES
				bAddress = request.POST.get("Address_ID")
				uAddress = Address.objects.get(Address_ID = bAddress)

				#PRIMARY DRIVER ATTRIBUTES
				dFname = request.POST.get("Driver_FirstName")
				dLname = request.POST.get("Driver_LastName")
				dEmail = request.POST.get("Driver_Email")
				dContactNumber = request.POST.get("Driver_ContactNumber")

				
				form = Driver(Driver_FirstName = dFname, Driver_LastName = dLname, Driver_Email = dEmail, Address_ID = uAddress, Driver_ContactNumber = dContactNumber)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR ORDER
	def AddOrder(request):
		if request.method == "POST":
			form = OrderForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#FOREIGN ORDER ATTRIBUTES
				bID = request.POST.get("User_ID")
				uID = User.objects.get(User_ID = bID)

				bDriverID = request.POST.get("Driver_ID")
				if (bDriverID):
					uDriverID = Driver.objects.get(Driver_ID = bDriverID)
				else:
					uDriverID = None
					
					
				

				#PRIMARY FOOD ATTRIBUTES
				oType = request.POST.get("Order_Type")
				oTotalCost = int(request.POST.get("Order_TotalCost"))
				Date = request.POST.get("Date")
				Time = request.POST.get("Time")

				form = Order(User_ID = uID, Order_Type = oType, Driver_ID = uDriverID, Order_TotalCost = oTotalCost, Date = Date, Time = Time)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
			else:
				print(form.errors)
				return HttpResponse('not valid')

	#FOR OrderItem
	def AddOrderItem(request):
		if request.method == "POST":
			form = OrderItemForm(request.POST)

			if form.is_valid():
				print(form.is_valid())
				#FOREIGN ORDER ITEM ATTRIBUTES
				bOrderID = request.POST.get("Order_ID")
				uOrderID = Order.objects.get(Order_ID = bOrderID)

				bFoodID = request.POST.get("Food_ID")
				uFoodID = Food.objects.get(Food_ID = bFoodID)
				

				#PRIMARY FOOD ATTRIBUTES
				quantity = int(request.POST.get("Quantity"))
				cost = int(request.POST.get("Cost"))

				form = OrderItem(Order_ID = uOrderID, Food_ID = uFoodID, Quantity = quantity, Cost = cost)
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
				