from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'foodies'
urlpatterns = [ 
#URLs for Foodies app
    #INDEX VIEWS
    path('', views.IndexView.as_view(), name="index"),
    path('register', views.IndexView.Register, name = "register"),
    path('login', views.IndexView.Login, name = "login"),



    #PROFILE VIEWS
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('logout', views.ProfileView.logout, name="logout"),

    #ORDERS VIEWS
    path('orders/', views.OrdersView.as_view(), name="orders"),



    #DASHBOARD VIEWS
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('createUser', views.DashboardView.AddUser, name = "userAdd"),
    path('createAddress', views.DashboardView.AddAddress, name="addressAdd"),
    path('createFood', views.DashboardView.AddFood, name="foodAdd"),
    path('createDriver', views.DashboardView.AddDriver, name="driverAdd"),
    path('createOrder', views.DashboardView.AddOrder, name="orderAdd"),
    path('Order', views.ProfileView.AddOrder, name="order"),
    path('orderItem', views.OrdersView.AddOrderItem, name="orderItem"),
    path('createOrderItem', views.DashboardView.AddOrderItem, name="orderItemAdd"),
    #path('updateUser', views.DashboardView.updateUser, name="userUpdate"),
    path('createRestaurant', views.DashboardView.AddRestaurant, name = "resAdd"),
]