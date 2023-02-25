from django.template import loader
from django.shortcuts import render
import json


from sustainable_app.models.user import User


# Sends view user data sorted by name, level and points
def leaderboard(request):


    #Gets leaderboard info ordered by username, level and points
    users = list(User.objects.order_by("username").values('username', 'xp', 'points'))
    users = add_users_level(users)
    level = list(User.objects.order_by("-xp").values('username', 'xp', 'points'))
    level = add_users_level(level)
    points = list(User.objects.order_by("-points").values('username', 'xp', 'points'))
    points = add_users_level(points)

    
    #Will send leaderboard info to html page for use by javascript
    context = {'name':json.dumps(users),'level': json.dumps(level),'points':json.dumps(points)}

   
    return render(request, "sustainable_app/leaderboard.html", context)
   

#Returns a dictionary that is the same as the one passed to it but the level of each user has been added to it
def add_users_level(dict):
    for user in dict:
        user['level'] = User.objects.get(username = user["username"]).level()

    return dict