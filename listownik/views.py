from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from passlib.hash import pbkdf2_sha256
from rest_framework.parsers import *
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password,make_password


class UserRegister(APIView):
    def post(self, request):
        users = User.objects.all()

        for var in users:
            if var.email == request.data['email']:
                return JsonResponse({'Error':'User already exists'},status=400)
            request.data['password'] = make_password(request.data['password'],salt=None,hasher='default')
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'Info':"Ok"},status=200)
            return JsonResponse({'Error':serializer.errors},status=400)

def checkpassword(data, user):
    users = User.objects.all()
    for var in users:
        if var.email == data['email']:
            if check_password(data['password'], var.password):
                return True
            return False

class LoginView(APIView):
    def post(self, request):
        users = User.objects.all()
        for var in users:
            if var.email == request.data['email']:
                if checkpassword(request.data, users):
                    return JsonResponse({'id': var.id}, status=200)
        return JsonResponse({'Error': 'User is not exists'}, status=400)


class UserDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShopView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class MeasureView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer

class MeasureDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer

class TypeView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class ProductView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = List.objects.all()
    serializer_class = ListSerializer

class ListDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class List_ProductView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = List_Product.objects.all()
    serializer_class = List_ProductSerializer

class List_ProductDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = List_Product.objects.all()
    serializer_class = List_ProductSerializer


class Shop_ProductView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = Shop_Product.objects.all()
    serializer_class = Shop_ProductSerializer

class Shop_ProductDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Shop_Product.objects.all()
    serializer_class = Shop_ProductSerializer


class SubscriptionView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class User_SubscriptionView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = User_Subscription.objects.all()
    serializer_class = User_SubscriptionSerializer

class User_SubscriptionDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = User_Subscription.objects.all()
    serializer_class = User_SubscriptionSerializer


class List_SubscriberView(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    queryset = List_Subscriber.objects.all()
    serializer_class = List_SubscriberSerializer

class List_SubscriberDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = List_Subscriber.objects.all()
    serializer_class = List_SubscriberSerializer

    # """
    # Retrieve, update or delete a user instance.
    # """
    # def get_object(self, pk):
    #     try:
    #         return User.objects.get(pk=pk)
    #     except User.DoesNotExist:
    #         raise Http404
    #
    # def post(self, request, format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def get(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     serializer = UserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)