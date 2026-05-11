# from django.http import HttpResponse
from django.shortcuts import render
from .serializers import UserRegistrationSerializer, BookingSerializer, MenuSerializer  
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import permissions 
from .models import Menu
from .models import Booking

from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def book(request):
    return render(request, 'book.html')
def reservations(request):
    bookings = Booking.objects.all()
    return render(request, 'reservations.html', {'bookings': bookings})
def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})
def display_menu_item(request, pk):
    menu_item = Menu.objects.get(pk=pk)
    return render(request, 'menu_item.html', {'menu_item': menu_item})
def bookings(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        reservation_date = request.POST.get('reservation_date')
        reservation_slot = request.POST.get('reservation_slot')
        number_of_guests = request.POST.get('number_of_guests')
        Booking.objects.create(
            first_name=first_name,
            reservation_date=reservation_date,
            reservation_slot=reservation_slot,
            number_of_guests=number_of_guests
        )
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})

class BookingView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MenuView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.AllowAny]



class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = serializer.get_token(user)
        return Response({
            'user': serializer.data,
            'token': token
        }, status=status.HTTP_201_CREATED)



