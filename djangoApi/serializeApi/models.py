from django.db import models

# Create your models here.


class Car(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.SmallIntegerField()
    barcode = models.CharField(max_length=255)
