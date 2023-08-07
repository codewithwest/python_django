from django.db import models

# Create your models here.


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)


class Athlete(models.Model):
    name = models.CharField(max_length=255)
    discipline = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
