from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from sustainable_app.models import DailyData, Goal



@login_required(login_url=reverse_lazy('login'))
def sorting(request):

    #Completing this goal for user
    user = request.user
    goal = Goal.objects.get(name = "sorting")
    DailyData.complete_goal(user, goal)
    
    return render(request, 'sustainable_app/sorting.html')
