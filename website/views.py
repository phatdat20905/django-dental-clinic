from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'website/home.html')

def login(request):
    return render(request, 'website/login.html')