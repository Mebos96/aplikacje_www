from django.conf.urls import url
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from . import views

urlpatterns = [
    #path('users/', views.UserView.as_view({'get': 'list', 'post': 'create'}), name='users'),
    path('user/<int:pk>', views.UserDetailView.as_view({'get': 'retrieve','patch':'partial_update', 'delete':'destroy'}), name='user'),

    path('register/', views.UserRegister.as_view(),name='register'),
    path('login/', views.LoginView.as_view(),name="login"),

    path('userLists/', views.UserLists.as_view(),name='userLists'),
    path('sharedLists/', views.SharedLists.as_view(),name='sharedLists'),

    path('username/', views.Username.as_view(), name='username'),

    path('shops/', views.ShopView.as_view({'get': 'list', 'post': 'create'}), name='shops'),
    path('shop/<int:pk>', views.ShopDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='shop'),

    path('measures/', views.MeasureView.as_view({'get': 'list', 'post': 'create'}), name='measures'),
    path('measure/<int:pk>', views.MeasureDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='measure'),

    path('types/', views.TypeView.as_view({'get': 'list', 'post': 'create'}), name='types'),
    path('type/<int:pk>',views.TypeDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='type'),

    path('products/', views.ProductView.as_view({'get': 'list', 'post': 'create'}), name='products'),
    path('product/<int:pk>',views.ProductDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='product'),

    path('lists/', views.ListView.as_view({'get': 'list', 'post': 'create'}), name='lists'),
    path('list/<int:pk>',views.ListDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='list'),

    path('list_products/', views.List_ProductView.as_view({'get': 'list', 'post': 'create'}), name='list_products'),
    path('list_product/<int:pk>', views.List_ProductDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='list_product'),

    path('shop_products/', views.List_ProductView.as_view({'get': 'list', 'post': 'create'}), name='shop_products'),
    path('shop_product/<int:pk>', views.List_ProductDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='shop_product'),

    path('subscriptions/', views.SubscriptionView.as_view({'get': 'list', 'post': 'create'}), name='subscriptions'),
    path('subscription/<int:pk>', views.SubscriptionDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='subscription'),

    path('user_subscriptions/', views.User_SubscriptionView.as_view({'get': 'list', 'post': 'create'}), name='user_subscriptions'),
    path('user_subscription/<int:pk>', views.User_SubscriptionDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='user_subscription'),

    path('list_subscribers/', views.List_SubscriberView.as_view({'get': 'list', 'post': 'create'}), name='list_subscribers'),
    path('list_subscriber/<int:pk>', views.List_SubscriberDetailView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),name='list_subscriber'),


    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'docs/', include_docs_urls('Docs')),
]