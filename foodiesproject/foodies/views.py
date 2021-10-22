from django.shortcuts import redirect, render
from django.db import transaction
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from django.http import HttpResponse, response

# Create your views here.
class IndexView(View):
	def get(self,request):
		return render(request,'index.html')

<<<<<<< Updated upstream
<<<<<<< Updated upstream
	#FOR REGISTER USER
	def RegisterUser(request):
		if request.method == "POST":
			form = UserForm(request.POST)
			
			if form.is_valid():
				print(form.is_valid())
				#FOREIGN USER ATTRIBUTES
				bAddress = request.POST.get("Address_ID")
				uAddress = Address.objects.get(Address_ID = bAddress)

				#PRIMARY USER ATTRIBUTES
=======
=======
>>>>>>> Stashed changes
	def register(request):
		if request.method == "POST":
			form = RegisterForm(request.POST)
			if form.is_valid():
				print(form.is_valid())
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
				uFname = request.POST.get("User_FirstName")
				uLname = request.POST.get("User_LastName")
				uPassword = request.POST.get("User_Password")
				uContactNumber = request.POST.get("User_ContactNumber")
				uEmail = request.POST.get("User_Email")

<<<<<<< Updated upstream
<<<<<<< Updated upstream
				
				form = User(User_FirstName = uFname, User_LastName = uLname, User_Password = uPassword, User_ContactNumber = uContactNumber, User_Email = uEmail, Address_ID = uAddress)
				form.save()
				messages.info(request, "Register Successful!")
				return redirect('http://127.0.0.1:8000/')
=======
=======
>>>>>>> Stashed changes
				aProvince = request.POST.get("Address_Province")
				aCity = request.POST.get("Address_City")
				aStreet = request.POST.get("Address_Street")

				form = Address(Address_Province = aProvince, Address_City = aCity, Address_Street = aStreet)
				form.save()

				uAddress = Address.objects.get(Address_Province = aProvince, Address_City = aCity, Address_Street = aStreet)
				print(uAddress)

				form = User(User_FirstName = uFname, User_LastName = uLname, User_Password = uPassword, User_ContactNumber = uContactNumber, User_Email = uEmail, Address_ID = uAddress)
				form.save()
				return redirect('http://127.0.0.1:8000/dashboard/')
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
			else:
				print(form.errors)
				return HttpResponse('not valid')

<<<<<<< Updated upstream
<<<<<<< Updated upstream
	#FOR LOGIN

	

=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
class RegisterView(View):
	def get(self,request):
		user = User.objects.all()
		address = Address.objects.all()
		context = {
			'user': user,
			'address': address
		}
		return render(request,'registration.html', context)

class ProfileView(View):
	def get(self,request):
		return render(request,'profile.html')

class DashboardView(View):
	def get(self,request):
		user = User.objects.all()
		restaurants = Restaurant.objects.all()
		address = Address.objects.all()
		food = Food.objects.all()
		driver = Driver.objects.all()
		order = Order.objects.all()
		orderItem = OrderItem.objects.all()
		resDesc = Restaurant.objects.values('Restaurant_Desc').distinct()
		
		countAmerican = Restaurant.objects.filter(Restaurant_Desc = 'American').count()
		countAsian = Restaurant.objects.filter(Restaurant_Desc = 'Asian').count()
		countCoffee = Restaurant.objects.filter(Restaurant_Desc = 'Coffee').count()
		countFilipino = Restaurant.objects.filter(Restaurant_Desc = 'Filipino').count()
		countCouple = Restaurant.objects.filter(Restaurant_Desc = 'Couple').count()
		addStreet = Address.objects.values('Address_City').distinct()
		countCebu = Address.objects.filter(Address_City = 'Cebu').count()
		countMandaue = Address.objects.filter(Address_City = 'Mandaue').count()
		context = {
			'user': user,
			'restaurants': restaurants,
			'address': address,
			'food': food,
			'driver': driver,
			'order': order,
			'orderItem': orderItem,
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

	#FOR UPDATE AND DELETE FUNCTIONS/METHODS
	#FOR UPDATE AND DELETE USER
	def post(self, request):
		if request.method == 'POST':
			#FOR USER
			if 'btnUpdateUser' in request.POST:
				print('User Update button clicked')
				usID = request.POST.get("User_ID")
				usFname = request.POST.get("User_FirstName")
				usLname = request.POST.get("User_LastName")
				usPassword = request.POST.get("User_Password")
				usContact = request.POST.get("User_ContactNumber")
				usEmail = request.POST.get("User_Email")
				usAddress = request.POST.get("Address_ID")

				update_user = User.objects.filter(User_ID = usID).update(User_FirstName = usFname, User_LastName = usLname, User_Password = usPassword, User_ContactNumber = usContact, User_Email = usEmail, Address_ID = usAddress)

				print(update_user)
				print('User Updated')
				return redirect('http://127.0.0.1:8000/dashboard/')
			elif 'btnDeleteUser' in request.POST:
				print('Delete Button for USER Clicked')
				usID = request.POST.get("User_ID")
				User.objects.filter(User_ID = usID).delete()
				print('USER Record Deleted')
				return redirect('http://127.0.0.1:8000/dashboard/')

			#FOR RESTAURANT
			elif 'btnUpdateRestaurant' in request.POST:
				print('Restaurant Update Button Clicked')
				resID = request.POST.get("Restaurant_ID")
				resName = request.POST.get("Restaurant_Name")
				resDesc = request.POST.get("Restaurant_Desc")
				resContact = request.POST.get("Restaurant_ContactNumber")
				resAddress = request.POST.get("Address_ID")

				update_restaurant = Restaurant.objects.filter(Restaurant_ID = resID).update(Restaurant_Name = resName, Restaurant_Desc = resDesc, Restaurant_ContactNumber = resContact, Address_ID = resAddress)
				print(update_restaurant)
				print('Restaurant Updated')
				return redirect('http://127.0.0.1:8000/dashboard/')
			elif 'btnDeleteRestaurant' in request.POST:
				print('Delete Button for RESTAURANT Clicked')
				resID = request.POST.get("Restaurant_ID")
				Restaurant.objects.filter(Restaurant_ID = resID).delete()
				print('RESTAURANT Record Deleted')
				return redirect('http://127.0.0.1:8000/dashboard/')

			#FOR ADDRESS
			elif 'btnUpdateAddress' in request.POST:
				print('Address Update Button Clicked')
				addID = request.POST.get("Address_ID")
				addProvince = request.POST.get("Address_Province")
				addCity = request.POST.get("Address_City")
				addStreet = request.POST.get("Address_Street")

				update_address = Address.objects.filter(Address_ID = addID).update(Address_Province = addProvince, Address_City = addCity, Address_Street = addStreet)
				print(update_address)
				print('Address Updated')
				return redirect('http://127.0.0.1:8000/dashboard/')
			elif 'btnDeleteAddress' in request.POST:
				print('Delete Button for ADDRESS Clicked')
				addID = request.POST.get("Address_ID")
				Address.objects.filter(Address_ID = addID).delete()
				print('ADDRESS Record Deleted')
				return redirect('http://127.0.0.1:8000/dashboard/')

			#FOR FOOD
			elif 'btnUpdateFood' in request.POST:
				print('Food Update Button Clicked')
				foodID = request.POST.get("Food_ID")
				rID = request.POST.get("Restaurant_ID")
				fName = request.POST.get("Food_Name")
				fDesc = request.POST.get("Food_Desc")
				fPrice = int(request.POST.get("Food_Price"))

				update_food = Food.objects.filter(Food_ID = foodID).update(Restaurant_ID = rID, Food_Name = fName, Food_Desc = fDesc, Food_Price = fPrice)
				print(update_food)
				print('food Updated')
				return redirect('http://127.0.0.1:8000/dashboard/')
			elif 'btnDeleteFood' in request.POST:
				print('Delete Button for FOOD Clicked')
				foodID = request.POST.get("Food_ID")
				Food.objects.filter(Food_ID = foodID).delete()
				print('FOOD Record Deleted')
				return redirect('http://127.0.0.1:8000/dashboard/')

			#FOR DRIVER
			elif 'btnUpdateDriver' in request.POST:
				print('Driver Update Button Clicked')
				driverID = request.POST.get("Driver_ID")
				dFirstName = request.POST.get("Driver_FirstName")
				dLastName = request.POST.get("Driver_LastName")
				dEmail = request.POST.get("Driver_Email")
				aID = request.POST.get("Address_ID")
				dContactNumber = request.POST.get("Driver_ContactNumber")

				update_driver = Driver.objects.filter(Driver_ID = driverID).update(Driver_FirstName = dFirstName, Driver_LastName = dLastName, Driver_Email = dEmail, Address_ID = aID, Driver_ContactNumber = dContactNumber)
				print(update_driver)
				print('driver Updated')
				return redirect('http://127.0.0.1:8000/dashboard/')
			elif 'btnDeleteDriver' in request.POST:
				print('Delete Button for DRIVER Clicked')
				driverID = request.POST.get("Driver_ID")
				Driver.objects.filter(Driver_ID = driverID).delete()
				print('DRIVER Record Deleted')
				return redirect('http://127.0.0.1:8000/dashboard/')

			#FOR ORDER
			elif 'btnUpdateOrder' in request.POST:
				print('Order Update Button Clicked')
				oID = request.POST.get("Order_ID")
				uID = request.POST.get("User_ID")
				oType = request.POST.get("Order_Type")
				dID = request.POST.get("Driver_ID")
				oTotalCost = request.POST.get("Order_TotalCost")
				date = request.POST.get("Date")
				time = request.POST.get("Time")

				update_order = Order.objects.filter(Order_ID = oID).update(User_ID = uID, Order_Type = oType, Driver_ID = dID, Order_TotalCost = oTotalCost, Date = date,Time = time)
				print(update_order)
				print('order Updated')
				return redirect('http://127.0.0.1:8000/dashboard/')
			elif 'btnDeleteOrder' in request.POST:
				print('Delete Button for ORDER Clicked')
				oID = request.POST.get("Order_ID")
				Order.objects.filter(Order_ID = oID).delete()
				print('Order Record Deleted')
				return redirect('http://127.0.0.1:8000/dashboard/')

			#FOR ORDER ITEM
			elif 'btnUpdateOrderItem' in request.POST:
				print('Order Item Update Button Clicked')
				oItemID = request.POST.get("OrderItem_ID")
				oID = request.POST.get("Order_ID")
				fID = request.POST.get("Food_ID")
				quanitity = int(request.POST.get("Quantity"))
				cost = int(request.POST.get("Cost"))

				update_order_item = OrderItem.objects.filter(OrderItem_ID = oItemID).update(Order_ID = oID, Food_ID = fID, Quantity = quanitity, Cost = cost)
				print(update_order_item)
				print('order item Updated')
				return redirect('http://127.0.0.1:8000/dashboard/')
			elif 'btnDeleteOrderItem' in request.POST:
				print('Delete Button for ORDER ITEM Clicked')
				oItemID = request.POST.get("OrderItem_ID")
				OrderItem.objects.filter(OrderItem_ID = oItemID).delete()
				print('Order Item Record Deleted')
				return redirect('http://127.0.0.1:8000/dashboard/')

			

				
			

			

	#FOR RESTAURANT
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



