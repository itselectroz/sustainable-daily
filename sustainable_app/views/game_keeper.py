from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

def game_keeper(request):
    return render(request, 'sustainable_app/game_keeper.html')