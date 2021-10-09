from django.urls import path
from . import views

#paths arranged alphabetically by name
app_name = 'foodies'
urlpatterns = [ 
#URLs for Foodies app
    path('', views.IndexView.as_view(), name="index"),
    path('dashboard/', views.DashboardView.as_view(), name="dashboard"),
    path('createUser', views.DashboardView.AddUser, name = "userAdd"),
    path('resRegister/', views.RestaurantRegisterView.as_view(), name = "resRegister_view"),
    path('createRestaurant', views.RestaurantRegisterView.AddRestaurant, name = "resAdd"),
]