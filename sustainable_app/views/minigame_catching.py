from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render


@login_required(login_url=reverse_lazy('login'))
def minigame_catching(request):
    return render(request, 'sustainable_app/minigame_catching.html')
