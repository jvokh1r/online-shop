import random
from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.timezone import now

from apps.users.models import CustomUser, UserAuthCode
from apps.users.services import send_email_to_user


def register_page(request):
    return render(request, 'register.html', {'error': False})


def send_code_to_email(request):
    error = False
    email, password, re_password = (request.POST.get('email'), request.POST.get('password'),
                                    request.POST.get('re_password'))

    if not (email and password and re_password):
        return redirect('register_page')

    if CustomUser.objects.filter(email=email).exists():
        error = True
        error_message = 'Email has already registered'

    elif password != re_password:
        error = True
        error_message = 'Passwords does not match!!!'

    if error:
        return render(request, 'register.html', {'email': email, 'error_message': error_message})

    code = random.randint(1000, 10000)
    send_email_to_user(email, code)
    UserAuthCode.objects.create(email=email, code=code, expire_at=now() + timedelta(minutes=5))
    context = {
        'email': email,
        'password': password,
        'code': '',
        'code_error': '',
        'error_message': '',
    }
    return render(request, 'confirm_email.html', context)


def register_user(request):
    code, email, password = request.POST.get('code'), request.POST.get('email'), request.POST.get('password')

    UserAuthCode.objects.filter(expire_at__lt=now()).delete()

    objs = UserAuthCode.objects.filter(code=code, email=email, expire_at__gte=now())

    if objs.exists():
        obj, created = CustomUser.objects.get_or_create(email=email)
        if created:
            obj.set_password(password)
        objs.delete()
    elif UserAuthCode.objects.filter(email=email, expire_at__gte=now()):
        context = {
            'email': email,
            'password': password,
            'code': code,
            'code_error': 'Code not valid',
        }
        return render(request, 'confirm_email.html', context)
    else:
        return redirect('register_page')
    return render(request, 'login.html')


def login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'User is not valid, please enter a valid email or password!!!')
        return redirect('home')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('home')
