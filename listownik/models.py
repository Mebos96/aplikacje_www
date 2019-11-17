from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class List(models.Model):
    name = models.CharField(max_length=30)


class Shop(models.Model):
    name = models.CharField(max_length=30)

class Measure(models.Model):
    name = models.CharField(max_length=30)
    short = models.CharField(max_length=10)

class Product(models.Model):
    name = models.CharField(max_length=30)
    unit_of_measure = models.ForeignKey(Measure,on_delete=models.CASCADE())
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE())
