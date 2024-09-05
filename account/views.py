from django.shortcuts import render
from .models import Profile

# Create your views here.

def signup_page(request):
    return render(request, 'account/signup.html')

def login_page(request):
    return render(request, 'account/login.html')

def show_profile(request):
    return render(request, 'account/profile.html')

def logout_page(request):
    return render(request, 'account/login.html')