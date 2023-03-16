import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from sustainable_app.models import Goal, DailyData, DailyGoalStatus
from sustainable_app.management.commands.dailytasks import Command
import random


"""To make a new goal create it with the same name as the page it is being created for. Give it the url to the page and the image for the daily goal. Go to the view being added
and add code to make it so the user gets a completed daily data whenever they play the game or do whatever e.g.
user = request.user
goal = Goal.objects.get(name = "minigame_catching")
DailyData.complete_goal(user, goal) """

@login_required(login_url=reverse_lazy('login'))
def home(request):

    # get current user
    current_user = request.user

    # pass goals to template
    personal_goals = Goal.objects.filter(type=Goal.PERSONAL)
    user_daily_completed_DGS = DailyGoalStatus.objects.filter(goal__active = True).filter(user_data__user = request.user).filter(completed = True)
    goal_ids = user_daily_completed_DGS.values_list('goal__id', flat=True)
    user_daily_completed = Goal.objects.filter(active=True, id__in=goal_ids)
    user_daily_notcompleted = Goal.objects.filter(active=True).exclude(dailygoalstatus__in=user_daily_completed_DGS)

    context = {
        "goals": personal_goals,
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
    

"""Updates daily goal"""
@login_required(login_url=reverse_lazy('login'))
def update_daily_goal_status(request):    
    if request.method == 'POST':
        # Get the current user and the score value from the POST request
        current_user = request.user
        score = request.POST.get('score')
        goal = request.POST.get('goal')


        # Update the corresponding DailyGoalStatus object
        try:
            current_goal = Goal.objects.get(name = goal)
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})


        dgs = DailyGoalStatus.objects.filter(user_data__user=current_user, goal=current_goal).first()

        #Makes sure doesnt overwrite a bigger score
        if (int(dgs.score) < int(score)):
            dgs.score = 5

        dgs.save()

        # Return a JSON response to indicate success
        return JsonResponse({'success': True})
    else:
        # Return an error response if the request is not valid
        return JsonResponse({'success': False, 'error': 'Invalid request'})
