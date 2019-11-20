from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    nick = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)


    # def validate_title(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError(
    #             "Blog post is not about Django",
    #         )
    #     return value

class ShopSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

class MeasureSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    short = serializers.CharField(max_length=10)

class Type(serializers.Serializer):
    name = serializers.CharField(max_length=50)

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=80)
    unit_of_measure = serializers.IntegerField()
    idType = serializers.IntegerField()
    idShop = serializers.IntegerField()

class ListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    favorite = serializers.BooleanField()
    idOwner = serializers.IntegerField()

class List_ProductSerializer(serializers.Serializer):
    idList = serializers.IntegerField()
    idProduct = serializers.IntegerField()
    isBought = serializers.BooleanField()

class Shop_ProductSerializer(serializers.Serializer):
    idShop = serializers.IntegerField()
    idProduct = serializers.IntegerField()

class SubscriptionSerializer(serializers.Serializer):
    idOwner = serializers.IntegerField()
    idList = serializers.IntegerField()
    idSubscription = serializers.IntegerField()

class User_SubscriptionSerializer(serializers.Serializer):
    idUser = serializers.IntegerField()
    idSubscription = serializers.IntegerField()

class List_SubscriberSerializer(serializers.Serializer):
    idList = serializers.IntegerField()
    idSubscription = serializers.IntegerField()