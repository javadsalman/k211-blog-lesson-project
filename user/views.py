from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                login(request, user)
                return redirect('info:home')
            return render(request, 'login.html', context={'form': form, 'invalid_credentials': True})
        return render(request, 'login.html', context={'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('info:home')
        return render(request, 'register.html', context={'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('user:login')