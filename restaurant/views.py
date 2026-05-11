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



