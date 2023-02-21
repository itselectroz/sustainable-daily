from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse


@login_required(login_url=reverse('login'))
def profile(request):
    return render(request, 'sustainable_app/profile.html')
