from django.contrib.auth import logout as user_logout
from django.shortcuts import redirect, reverse


def logout(request):
    user_logout(request)
    return redirect(reverse('login'))
