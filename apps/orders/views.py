from django.shortcuts import render


def checkout(request):
    active_page = 'checkout'
    ctx = {
        'active_page': active_page,
    }
    return render(request, 'checkout.html', ctx)
