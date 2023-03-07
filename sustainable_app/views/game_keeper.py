from django.shortcuts import render, redirect, reverse
from sustainable_app.models.user import User

def game_keeper(request):
    if(request.user.is_authenticated):
        if(request.user.game_keeper):
        
            context = {
                "game_keepers":  User.objects.filter(game_keeper=True)
            }
            
            return render(request, 'sustainable_app/game_keeper.html', context)
        else:
            return redirect(reverse('home'))
    else:
       return redirect(reverse('login'))
   
def game_keeper_locations(request):
    if(request.user.is_authenticated):
        if(request.user.game_keeper):
            return render(request, 'sustainable_app/game_keeper_locations.html')
        else:
            return redirect(reverse('home'))
    else:
       return redirect(reverse('login'))

def game_keeper_surveys(request):
    if(request.user.is_authenticated):
        if(request.user.game_keeper):
            return render(request, 'sustainable_app/game_keeper_surveys.html')
        else:
            return redirect(reverse('home'))
    else:
       return redirect(reverse('login'))

def game_keeper_events(request):
    if(request.user.is_authenticated):
        if(request.user.game_keeper):
            return render(request, 'sustainable_app/game_keeper_events.html')
        else:
            return redirect(reverse('home'))
    else:
       return redirect(reverse('login'))

# Remove keeper request
def remove_keeper(request):
    username = request.POST.get('username', False)
    User.objects.get(username=username).delete()
    return redirect('/')