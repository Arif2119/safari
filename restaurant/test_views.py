from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from .models import Booking, Menu

class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            first_name='John',
            reservation_date=date(2024, 6, 30),
            reservation_slot=10,
            number_of_guests=2
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.first_name, 'John')
        self.assertEqual(self.booking.reservation_date, date(2024, 6, 30))
        self.assertEqual(self.booking.reservation_slot, 10)
        self.assertEqual(self.booking.number_of_guests, 2)

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title='Test Item',
            price=10.99,
            inventory=100
        )

    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.title, 'Test Item')
        self.assertEqual(self.menu_item.price, 10.99)
        self.assertEqual(self.menu_item.inventory, 100) 
class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='Testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_booking_api(self):
        response = self.client.post('/api/bookings/', {
            'first_name': 'John',
            'reservation_date': '2024-06-30',
            'reservation_slot': 10,
            'number_of_guests': 2
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_menu_api(self):
        Menu.objects.create(title='Test Item', price=10.99, inventory=100)
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
