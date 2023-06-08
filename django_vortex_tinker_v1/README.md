# Django 101

### accessing the django shell python manage.py shell

### Creating model

from django.db import models

# Create your models[app level models.py].

> ### class Menu(models.Model):
>
> > ### name = models.CharField(max_length=100)
>
> > ### cuisine = models.CharField(max_length=100)
>
> > ### price = models.IntegerField()

> > ### def **str**(self) -> str:
>
> > ### return self.name + " : " + self.cuisine

>

# Add To App installed List[project levels settings.py]

### INSTALLED_APPS = [

     ...
    'vortex_tinker.apps.VortexTinkerConfig',
     ]

### Making Migrations

> python.exe .\manage.py makemigrations

### Migrating

> python.exe .\manage.py migrate

# database query in shell adding values

> #### from vortex_tinker.models import Menu
>
> #### Menu.objects.all()
>
> #### <QuerySet []>

> #### m = Menu.object.create(name="kota", cuisine ="sa", price="200")

> #### m = Menu.objects.create(name="kota", cuisine ="sa", price="200")
>
> #### m = Menu.objects.create(name="sphahlo", cuisine ="velo", price="200")
>
> #### Menu.objects.all()

# Updating values in database

> #### from vortex_tinker.models import Menu

> #### p = Menu.objects.get(pk=2)

> #### p.cuisine = "new value"

> #### p.save()

> #### Menu.objects.all()
>
> #### <QuerySet [<Menu: kota : sa>, <Menu: sphahlo : new value>]>
