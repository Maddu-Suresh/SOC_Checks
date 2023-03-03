from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#function for home

def login(request):
    return render(request, 'login.html')