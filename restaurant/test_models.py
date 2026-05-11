from datetime import date
from django.test import TestCase
from .models import Booking, Menu
# Create your tests here.
class BookingModelTest(TestCase):
    def test_booking_string_representation(self):
        booking = Booking.objects.create(
            first_name='Mario',
            reservation_date=date(2026, 5, 22),
            reservation_slot=18,
            guests=2,
        )
        self.assertIn('Mario', str(booking))
class MenuModelTest(TestCase):
    def test_menu_string_representation(self):
        menu_item = Menu.objects.create(
            name='Pasta',
            price=12,
            menu_item_description='Delicious pasta with tomato sauce.'
        )
        self.assertIn('Pasta', str(menu_item))  