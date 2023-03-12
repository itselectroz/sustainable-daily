
from django.template import loader
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from sustainable_app.models.user import User

# Dictionaries

background_dict = {
    "b_green": "#65d982",
    "b_grey": "#858186",
    "b_pink": "#dd69e7",
    "b_blue": "#17a3c9",
    "b_white": "#ffffff",
}

username_dict = {
    "u_green": "#14820a",
    "u_black": "#000000",
    "u_purple": "#5f0b7b",
    "u_blue": "#192e6c",
    "u_orange": "#ed8114",
}


# Sends view user data sorted by name, level and points
@login_required(login_url=reverse_lazy('login'))
def leaderboard(request):


    #Gets leaderboard info ordered by username, level and points
    users = list(User.objects.order_by("username").values('username', 'xp', 'points'))
    users = add_users_level(users)
    equipped_items_by_username = User.objects.order_by("username").prefetch_related('equipped_items')
    users = add_equipped_items(users,equipped_items_by_username)

    level = list(User.objects.order_by("-xp").values('username', 'xp', 'points'))
    level = add_users_level(level)
    equipped_items_by_level = User.objects.order_by("-xp").prefetch_related('equipped_items')
    level = add_equipped_items(level,equipped_items_by_level)
    
    points = list(User.objects.order_by("-points").values('username', 'xp', 'points'))
    points = add_users_level(points)
    equipped_items_by_points = User.objects.order_by("-points").prefetch_related('equipped_items')
    points = add_equipped_items(points,equipped_items_by_points)

    
    #Will send leaderboard info to html page for use by javascript
    context = {'name':json.dumps(users),'level': json.dumps(level),'points':json.dumps(points)}

   
    return render(request, "sustainable_app/leaderboard.html", context)
   

#Returns a dictionary that is the same as the one passed to it but the level of each user has been added to it
def add_users_level(user_dict):
    for user in user_dict:
        user['level'] = User.objects.get(username = user["username"]).level()

    return user_dict

#Returns a dictionary that is the same as the one passed to it but the equipped items of each user has been added to it
def add_equipped_items(users,user_equipped_items):
    for i, user in enumerate(users):
        equipped_items = list(user_equipped_items[i].equipped_items.values_list('type', 'name'))
        #Sets default
        user['character'] = "badger"
        user['accessory'] = "none"
        user['background_color'] = background_dict[str("b_white")]
        user['username_color'] = username_dict[str("u_black")]
        if equipped_items:
            
            for item in equipped_items:
                if item[0] == 'character':
                    user['character'] = item[1]

                if item[0] == 'accessory':
                    user['accessory'] = item[1]

                if item[0] == 'background_color':
                    user['background_color'] = background_dict[str(item[1])]

                if item[0] == 'username_color':
                    user['username_color'] = username_dict[str(item[1])]

    return users
