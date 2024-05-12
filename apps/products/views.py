from django.shortcuts import render
from .models import Product
from apps.features.models import Feature


def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    features = Feature.objects.all().order_by('-ordering_number')
    ctx = {
        'products': products,
        'features': features,
    }
    return render(request, 'products/product_list.html', ctx)


def product_detail(request):
    return render(request, 'products/product_detail.html')
