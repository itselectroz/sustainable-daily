from django.shortcuts import render, redirect, reverse
from sustainable_app.models.user import User

# game keeper page
def game_keeper(request):
    
    # send all game keepers to template
    context = {
        "game_keepers":  User.objects.filter(game_keeper=True)
    }
    
    return direct_user("", request, context) 
   
# game keeper locations page
def game_keeper_locations(request):
    return direct_user("_locations", request, {})

def game_keeper_surveys(request):
    return direct_user("_surveys", request, {})

def game_keeper_events(request):
    return direct_user("_events", request, {})

# Remove keeper request
def remove_keeper(request):
    # get username from post request
    username = request.POST.get('username', False)
    # delete user with given username
    User.objects.get(username=username).delete()
    # refresh the page
    return redirect('/')

# direct user to correct page
def direct_user(page, request, context):
    # if user is authenticated
    if(request.user.is_authenticated):
        # if user is a game keeper
        if(request.user.game_keeper):
            # render game keeper locations page
            return render(request, 'sustainable_app/game_keeper' + page + '.html', context)
        else:
            # render home page
            return redirect(reverse('home'))
    else:
        # render login
        return redirect(reverse('login'))