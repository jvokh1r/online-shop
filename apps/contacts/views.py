from django.shortcuts import render


def contact(request):
    active_page = 'contact'
    ctx = {
        'active_page': active_page,
    }
    return render(request, 'contact.html', ctx)
