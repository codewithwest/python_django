from django.db import models

# Create your models here.




class MenuCategory(models.Model):
    menu_categoty_name = models.CharField(max_length=200)

# class Menu(models.Model):
#     menu_item =models.CharField(max_length=200)
#     price = models.IntegerField(null=False)
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)


    def __str__(self) -> str:
        return self.name + " : " + self.cuisine

class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self) -> str:
        return self.name

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name