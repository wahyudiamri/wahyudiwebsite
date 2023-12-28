from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())

def keranjang(request):
    return render(request,'keranjang.html')

def Checkout(request):
    return render(request,'Checkout.html')

def pesan(request):
    return render(request,'pesan.html')

def login(request):
    return render(request,'login.html')