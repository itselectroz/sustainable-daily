import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from sustainable_app.models import Goal, DailyData, User, DailyGoalStatus



@login_required(login_url=reverse_lazy('login'))
def home(request):

    # get current user
    current_user = request.user

    # pass goals to template
    personal_goals = Goal.objects.filter(type=Goal.PERSONAL)
    context = {
        "goals": personal_goals,
        "streak": request.user.streak_length

    }

    
    

    context["completed"] = getTodayCompleted(current_user)
    
    #TODO: Use randomly picked goals, not all goals
    return render(request, 'sustainable_app/home.html', context)

def complete_personal(request):

    goal_id = request.POST.get('goal_id', False)
    goal = Goal.objects.get(id=goal_id)

    # check if goal already completed
    if goal not in getTodayCompleted(request.user):
        DailyData.complete_goal(request.user, goal)

        return HttpResponse(status=200)
    

def getTodayCompleted(user):
# get user's completed goals
    today = datetime.date.today()
    try:
        daily_data = DailyData.objects.get(date=today, user=user)
        completed_goals = daily_data.daily_goals.filter(dailygoalstatus__completed=True)
        return completed_goals
        
    except DailyData.DoesNotExist:
        return []