from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvForm


def index(request):
    adv = Advertisement.objects.all()
    context = {
        'advertisements': adv
    }
    return render(request, 'app_sauldspagetti/index.html',context)

def top(request):
    return render(request,'app_sauldspagetti/top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvForm()
    context={'form': form}
    return render(request, 'app_sauldspagetti/advertisement-post.html', context)

# Create your views here.
