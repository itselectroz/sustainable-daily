from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.shortcuts import redirect, render, reverse


def authenticate_request(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if not username or not password:
        return False

    user = authenticate(request, username=username, password=password)

    if user is not None:
        user_login(request, user)
        # TODO: change this to home when home page is done
        return redirect(reverse('profile'))
    else:
        return redirect(reverse('login') + '?error=1')


def login(request):
    if request.user.is_authenticated:
        # TODO: change this to home when home page is done
        return redirect(reverse('profile'))

    if request.method == "POST" and request.POST is not None:
        response = authenticate_request(request)
        if response is not False:
            return response

    return render(request, 'sustainable_app/login.html')
