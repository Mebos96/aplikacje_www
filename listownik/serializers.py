from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    # nick = serializers.CharField(max_length=30)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=30)

    class Meta:
        model = User
        fields = '__all__'

    # def validate_title(self, value):
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError(
    #             "Blog post is not about Django",
    #         )
    #     return value


class ShopSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=30)

    class Meta:
        model = Shop
        fields = '__all__'



class MeasureSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=30)
    # short = serializers.CharField(max_length=10)

    class Meta:
        model = Measure
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=50)

    class Meta:
        model = Type
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=80)
    # unit_of_measure = serializers.PrimaryKeyRelatedField(read_only=True)
    # idType = serializers.PrimaryKeyRelatedField(read_only=True)
    # idShop = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=30)
    # favorite = serializers.BooleanField()
    # idOwner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = List
        fields = '__all__'


class List_ProductSerializer(serializers.ModelSerializer):
    # idList = serializers.PrimaryKeyRelatedField(read_only=True)
    # idProduct = serializers.PrimaryKeyRelatedField(read_only=True)
    # isBought = serializers.BooleanField()

    class Meta:
        model = List_Product
        fields = '__all__'


class Shop_ProductSerializer(serializers.ModelSerializer):
    # idShop = serializers.PrimaryKeyRelatedField(read_only=True)
    # idProduct = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Shop_Product
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    # idOwner = serializers.PrimaryKeyRelatedField(read_only=True)
    # idList = serializers.PrimaryKeyRelatedField(read_only=True)
    # idSubscription = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'


class User_SubscriptionSerializer(serializers.ModelSerializer):
    # idUser = serializers.PrimaryKeyRelatedField(read_only=True)
    # idSubscription = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User_Subscription
        fields = '__all__'


class List_SubscriberSerializer(serializers.ModelSerializer):
    # idList = serializers.PrimaryKeyRelatedField(read_only=True)
    # idSubscription = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = List_Subscriber
        fields = '__all__'