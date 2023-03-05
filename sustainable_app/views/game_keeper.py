from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy

def game_keeper(request):
    if(request.user.is_authenticated):
        if(request.user.game_keeper):
            return render(request, 'sustainable_app/game_keeper.html')
        else:
            return redirect(reverse('home'))
    else:
       return redirect(reverse('login'))
   
def game_keeper_locations(request):
    return render(request, 'sustainable_app/game_keeper_locations.html')

def game_keeper_surveys(request):
    return render(request, 'sustainable_app/game_keeper_surveys.html')

def game_keeper_events(request):
    return render(request, 'sustainable_app/game_keeper_events.html')