from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('auth/', views.auth, name="auth"),
    path('catalog/', views.catalog, name="catalog"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('orders/', views.orders, name="orders"),
    path('success/', views.success, name="success"),
    path('error/', views.error, name="error"),
    path('adduser/', views.addUser, name="adduser"),
    path('addtocart/', views.addToCart, name="addtocart"),
    path('addtoorders/', views.addToOrders, name="addtoorders"),
    path('ordernow/', views.orderNow, name="ordernow")
]
