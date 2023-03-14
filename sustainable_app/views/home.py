import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from sustainable_app.models import Goal, DailyData, DailyGoalStatus
import random




@login_required(login_url=reverse_lazy('login'))
def home(request):

    randomize_daily_goals()

    # get current user
    current_user = request.user

    # pass goals to template
    personal_goals = Goal.objects.filter(type=Goal.PERSONAL)
    u_goals = Goal.objects.filter(active = True)
    user_daily_completed_DGS = DailyGoalStatus.objects.filter(goal__active = True).filter(user_data__user = request.user).filter(completed = True)
    goal_ids = user_daily_completed_DGS.values_list('goal__id', flat=True)
    user_daily_completed = Goal.objects.filter(active=True, id__in=goal_ids)
    user_daily_notcompleted = Goal.objects.filter(active=True).exclude(dailygoalstatus__in=user_daily_completed_DGS)

    print("ugoals:", u_goals, " completed: ",user_daily_completed , "########")


    context = {
        "goals": personal_goals,
        "u_goals": u_goals,
        "user_daily_completed" : user_daily_completed,
        "user_daily_notcompleted" : user_daily_notcompleted
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
    
def randomize_daily_goals() :
    #Set 5 random daily goals to active
    u_goals = Goal.objects.exclude(type=Goal.PERSONAL)

    #Setting all goals to inactive 
    for goal in u_goals:
        goal.active = False
        goal.save()
    
    #Setting 5 random goals to active
    all_goals = u_goals.order_by('?')[:2]

    print(all_goals)

    for goal in all_goals:
        goal.active = True
        goal.save()

    

