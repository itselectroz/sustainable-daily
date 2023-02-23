from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login

from ..models import User


def register_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    first_name = request.POST.get('first-name', '')
    last_name = request.POST.get('last-name', '')
    email = request.POST.get('email', '')

    for var in [username, password, first_name, last_name, email]:
        if not var:
            # TODO: better error here
            return redirect(reverse('register') + "?error=1")

    user = User.objects.create_user(username, email, password)

    user.first_name = first_name
    user.last_name = last_name

    user.save()

    login(request, user)

    return redirect(reverse('home'))


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST" and request.POST is not None:
        return register_user(request)

    return render(request, 'sustainable_app/register.html')
