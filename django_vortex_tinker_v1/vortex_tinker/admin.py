from django.contrib import admin

# Register your models here.
from .models import Menu, MenuCategory, Booking, Employee

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Employee)
admin.site.register(Booking)


# Command to perform migrations
# python3 manage.py makemigrations
# python3 manage.py migrate

# Command to run server
# python3 manage.py runserver

# Command to create a super user
# python3 manage.py createsuperuser
