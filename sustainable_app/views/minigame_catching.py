from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sustainable_app.models import DailyData, Goal


#@login_required(login_url='/login')
def minigame_catching(request):

    #Completing this goal for user
    user = request.user
    goal = Goal.objects.get(name = "minigame_catching")
    DailyData.complete_goal(user, goal)


    return render(request, 'sustainable_app/minigame_catching.html')
