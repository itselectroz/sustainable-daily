from django.contrib.auth import logout as user_logout
from django.shortcuts import redirect, reverse


def logout(request):
    """
    Logs the current user out of their account and redirects them to login
    """
    user_logout(request)
    return redirect(reverse('login'))
