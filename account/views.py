from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def signup_page(request):
    try:
        if request.method == 'POST':
            profile_pic = request.FILES.get('profile')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            con_password = request.POST.get('confirm_password')

            user_obj = User.objects.filter(email = email)

            if user_obj.exists():
                messages.success(request, 'Email already exist!')
                return render(request, 'account/signup.html')
            
            elif password != con_password:
                messages.success(request, 'Password missmatch!')
                return render(request, 'account/signup.html')
            else:
                user_create_obj = User.objects.create(
                    first_name = username,
                    username = email,
                    email = email
                )
                user_create_obj.set_password(password)
                user_create_obj.save()

                if user_create_obj:
                    profile = Profile.objects.create(
                        picture = profile_pic,
                        user = user_create_obj
                    )
                    profile.save()
                    return redirect('/login')
                    
        return render(request, 'account/signup.html')
    except Exception as e:
        print(e)
        return render(request, 'account/signup.html')
        

def login_page(request):
    try:
        if request.method == 'POST':

            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username = email, password = password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.success(request, 'Something went wrong login failed!')
                return render(request, 'account/login.html')
            
        return render(request, 'account/login.html')
    except Exception as e:
        print(e)
    return render(request, 'account/login.html')

def show_profile(request):
    return render(request, 'account/profile.html')

def logout_page(request):
    logout(request)
    return redirect('/login')