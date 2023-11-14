from django.urls import path
from .views import home,kontak


urlpatterns=[
    path('',home, name='home.html'),
    path('kontak',kontak, name='kontak.html'),
]