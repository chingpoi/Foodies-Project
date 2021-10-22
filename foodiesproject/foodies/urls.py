from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'foodies'
urlpatterns = [ 
#URLs for Foodies app
    path('', views.IndexView.as_view(), name="index"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('createUser', views.DashboardView.AddUser, name = "userAdd"),
    path('createAddress', views.DashboardView.AddAddress, name="addressAdd"),
    path('createFood', views.DashboardView.AddFood, name="foodAdd"),
    path('createDriver', views.DashboardView.AddDriver, name="driverAdd"),
    path('createOrder', views.DashboardView.AddOrder, name="orderAdd"),
    path('createOrderItem', views.DashboardView.AddOrderItem, name="orderItemAdd"),
    #path('updateUser', views.DashboardView.updateUser, name="userUpdate"),
    path('resRegister/', views.RestaurantRegisterView.as_view(), name = "resRegister_view"),
    path('createRestaurant', views.DashboardView.AddRestaurant, name = "resAdd"),
]