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
            return redirect(reverse('register') + "?error=1") # TODO: better error here
    
    user = User.objects.create_user(username, email, password)

    user.first_name = first_name
    user.last_name = last_name

    user.save()
    
    login(request, user)

    # TODO: change to home
    return redirect(reverse('profile'))



def register(request):
    if request.user.is_authenticated:
        # TODO: change this to home when home page is done
        return redirect(reverse('profile'))

    if request.method == "POST" and request.POST is not None:
        return register_user(request)

    return render(request, 'sustainable_app/register.html')
