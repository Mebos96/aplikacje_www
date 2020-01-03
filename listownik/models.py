
from django.db import models

# Create your models here.

#Użyty
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.name

class Measure(models.Model):
    name = models.CharField(max_length=30,unique=True)
    short = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=80)
    unit_of_measure = models.ForeignKey(Measure,on_delete=models.CASCADE)
    idType = models.ForeignKey(Type,on_delete=models.CASCADE)
    idShop = models.ForeignKey(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Użyty
class List(models.Model):
    name = models.CharField(max_length=30)
    favorite = models.BooleanField(default=False)
    idOwner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class List_Product(models.Model):
    idList = models.ForeignKey(List,on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    isBought = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Shop_Product(models.Model):
    idShop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Użyty
class Subscription(models.Model):
    idOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Owner')
    idList = models.ForeignKey(List, on_delete=models.CASCADE)
    idSubscription = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Subscriber')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User_Subscription(models.Model):
    idUser = models.ForeignKey(User,on_delete=models.CASCADE)
    idSubscription = models.ForeignKey(Subscription,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class List_Subscriber(models.Model):
    idList = models.ForeignKey(List, on_delete=models.CASCADE)
    idSubscription = models.ForeignKey(Subscription,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
