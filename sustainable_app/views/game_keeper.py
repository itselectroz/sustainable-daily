from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

def game_keeper(request):
    return render(request, 'sustainable_app/game_keeper.html')

def game_keeper_locations(request):
    return render(request, 'sustainable_app/game_keeper_locations.html')

def game_keeper_surveys(request):
    return render(request, 'sustainable_app/game_keeper_surveys.html')

def game_keeper_events(request):
    return render(request, 'sustainable_app/game_keeper_events.html')