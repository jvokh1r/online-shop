from django.shortcuts import render
from .models import General


def general(request):
    data = General.objects.first()
    ctx = {
        'data': data,
    }
    return render(request, 'base.html', ctx)


def home(request):
    active_page = 'home'
    store_data = General.objects.first()
    ctx = {
        'store_data': store_data,
        'active_page': active_page
    }
    return render(request, 'index.html', ctx)



