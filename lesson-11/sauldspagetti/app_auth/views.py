from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import RegForm

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найден"})

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RegForm()
    return render(request, 'app_auth/register.html', {'reg_form':form})