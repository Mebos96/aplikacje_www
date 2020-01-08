from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.parsers import *
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password,make_password
from .models import *
#import djoser

class UserRegister(APIView):
    def post(self, request):
        abc = User.objects.filter(email=request.data['email']).values()
        if len(abc) > 0:
            return JsonResponse({'Error': 'User already exists'}, status=400)
        else:
            request.data['password'] = make_password(request.data['password'], salt=None, hasher='default')
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'Info': "Ok"}, status=200)
            return JsonResponse({'Error': serializer.errors}, status=404)

def checkpassword(data, users):
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

class UserLists(APIView):
    def post(self, request):
        queryset = List.objects.filter(idOwner_id=int(request.data['idUser'])).values()
        return JsonResponse({"data": list(queryset)}, status=200)

class SharedLists(APIView):
    def post(self, request):
        subscriptions = Subscription.objects.filter(idSubscription=int(request.data['idUser'])).values()
        lists = List.objects.values()
        data = []
        for sub in subscriptions:
            for lis in lists:
                if sub['idList_id'] == lis['id']:
                    user = User.objects.filter(id=lis['idOwner_id']).values('username')
                    lis['favorite'] = sub['favorite']
                    lis['username'] = user[0]['username']
                    lis['idSub'] = sub['id']
                    data.append(lis)
        return JsonResponse({"data": list(data)}, status=200)

class Username(APIView):
    def post(self,request):
        users = User.objects.values()
        data = []
        for user in users:
            if request.data['name'] != '':
                if request.data['name'].lower() in user['username'].lower():
                    data.append(user)
        return JsonResponse({"data": list(data[:10])}, status=200)

class ProductName(APIView):
    def post(self,request):
        products = Product.objects.values()
        data = []
        for product in products:
            if request.data['name'] != '':
                if request.data['name'].lower() in product['name'].lower():
                    data.append(product)
        return JsonResponse({"data": list(data[:5])}, status=200)

class ShopName(APIView):
    def post(self,request):
        shops = Shop.objects.values()
        data = []
        for shop in shops:
            if request.data['name'] != '':
                if request.data['name'].lower() in shop['name'].lower():
                    data.append(shop)
        return JsonResponse({"data": list(data[:5])}, status=200)

class LastListId(APIView):
    def get(self, request):
        obj = List.objects.values()
        id = obj[len(obj)-1]
        return JsonResponse({"id": id['id']},status = 200)

class UserDetailView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        try:
            request.data['password'] = make_password(request.data['password'], salt=None, hasher='default')
            return self.update(request, *args, **kwargs)
        except:
            return self.update(request, *args, **kwargs)


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