from django.shortcuts import render


def cart(request):
    active_page = 'cart'
    ctx = {
        'active_page': active_page,
    }
    return render(request, 'cart.html', ctx)