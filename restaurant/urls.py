from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('api/bookings/', views.BookingView.as_view(), name='booking'),
    path('api/menu/', views.MenuView.as_view(), name='menu'),
    path('api-token-auth/', views.UserRegistrationView.as_view(), name='register'),
]