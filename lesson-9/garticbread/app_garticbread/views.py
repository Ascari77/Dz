from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

# Create your views here.

def index(request):
    adv = Advertisement.objects.all()
    context = {
        'advertisements': adv
    }
    return render(request, 'index.html',context)
def top(request):
    return render(request, 'top-sellers.html')
def advertisement_post(request):
    return render(request, 'advertisement-post.html')
def registration(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')
# Create your views here.
