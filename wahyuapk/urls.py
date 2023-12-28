from django.urls import path
from .views import home,Checkout,pesan,keranjang,login


urlpatterns=[
    path('',home, name='home.html'),
    path('pesan',pesan, name='pesan.html'),
    path('keranjang',keranjang, name='keranjang.html'),
    path('Checkout',Checkout, name='Checkout.html'),
    path('login',login, name='login.html'),
]