from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('products/',products,name='products'),
    path('customer/<str:pk>/',customer,name='customer'),
    path('createorder/<str:pk>/',createOrder,name='createorder'),
    path('createorder/<str:pk>/',UpdateOrder,name='updateorder'),
    path('deleteorder/<str:pk>/',deleteOrder,name='deleteorder'),
]