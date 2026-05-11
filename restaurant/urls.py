from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('api/bookings/', views.BookingView.as_view(), name='booking'),
    path('api/menu/', views.MenuView.as_view(), name='menu'),
    path('api/register/', views.UserRegistrationView.as_view(), name='register'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    path('menu/', views.menu, name='menu'),
    path('menu/<int:pk>/', views.display_menu_item, name='display_menu_item'),
    path('bookings/', views.bookings, name='bookings'),
]