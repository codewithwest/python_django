from django.test import TestCase
from datetime import datetime
from .models import Menu
# Create your tests here.

class MenuTestCase(TestCase):
    @classmethod
    def setUpTestdata(cls):
        cls.menu = Menu.objects.create(
            name="west",
            cuisine="nice",
           
        )
    def test_fields(self):
        self.assertIsInstance(self.menu.name,str)
        self.assertIsInstance(self.menu.price,str)
