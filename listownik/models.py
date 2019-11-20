from django.db import models

# Create your models here.

class User(models.Model):
    nick = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Shop(models.Model):
    name = models.CharField(max_length=30,unique=True)

class Measure(models.Model):
    name = models.CharField(max_length=30,unique=True)
    short = models.CharField(max_length=10)

class Type(models.Model):
    name = models.CharField(max_length=50,unique=True)

class Product(models.Model):
    name = models.CharField(max_length=80)
    unit_of_measure = models.ForeignKey(Measure,on_delete=models.CASCADE)
    idType = models.ForeignKey(Type,on_delete=models.CASCADE)
    idShop = models.ForeignKey(Shop,on_delete=models.CASCADE)

class List(models.Model):
    name = models.CharField(max_length=30)
    favorite = models.BooleanField(default=False)
    idOwner = models.ForeignKey(User, on_delete=models.CASCADE)

class List_Product(models.Model):
    idList = models.ForeignKey(List,on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    isBought = models.BooleanField(default=False)

class Shop_Product(models.Model):
    idShop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product,on_delete=models.CASCADE)

class Subscription(models.Model):
    idOwner = models.ForeignKey(User,on_delete=models.CASCADE, related_name='Owner')
    idList = models.ForeignKey(List,on_delete=models.CASCADE)
    idSubscription = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Subscriber')

class User_Subscription(models.Model):
    idUser = models.ForeignKey(User,on_delete=models.CASCADE)
    idSubscription = models.ForeignKey(Subscription,on_delete=models.CASCADE)

class List_Subscriber(models.Model):
    idList = models.ForeignKey(List, on_delete=models.CASCADE)
    idSubscription = models.ForeignKey(Subscription,on_delete=models.CASCADE)
