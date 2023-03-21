import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from sustainable_app.models import Goal, DailyData, Statistics


"""
To make a new goal create it with the same name as the page it is being created for.
Give it the url to the page and the image for the daily goal.

Go to the view being added, and add code to make it so the user gets a
completed daily data whenever they play the game or do whatever e.g.

user = request.user
goal = Goal.objects.get(name = "minigame_catching")
DailyData.complete_goal(user, goal)
"""

# Views

@login_required(login_url=reverse_lazy('login'))
def home(request):
    """
    Sends goals and current user's streak to template
    """

    # get current user
    current_user = request.user

    # pass goals to template
    daily_goals = Goal.objects.exclude(type=Goal.PERSONAL).filter(active=True)
    personal_goals = Goal.objects.filter(type=Goal.PERSONAL)

    context = {
        "daily_goals": daily_goals,
        "personal_goals": personal_goals,
        "completed": get_completed_goals(current_user),
        "streak": current_user.streak_length
    }
    
    return render(request, 'sustainable_app/home.html', context)


def complete_personal(request):
    """
    Updates personal goal to completed
    """

    if not request.user or not request.user.is_authenticated:
            raise HttpResponseForbidden()

    goal_id = request.POST.get('goal_id', False)
    goal = Goal.objects.get(id=goal_id, type=Goal.PERSONAL)

    # check if goal already completed
    if goal not in get_completed_goals(request.user):
        DailyData.complete_goal(request.user, goal)

        return HttpResponse(status=200)

def update_water(request):
    if not request.user or not request.user.is_authenticated:
        raise HttpResponseForbidden()

    Statistics.increment_quantity("water")
    return HttpResponse(status=200)

def update_recycle(request):
    Statistics.increment_quantity("plastic")
    return HttpResponse(status=200)
    

def update_daily_goal_status(request):
    """
    Completes a daily goal, errors if the goal does not exist.
    """

    if not request.user or not request.user.is_authenticated:
        raise HttpResponseForbidden()

    if request.method == 'POST':
        # Get the current user and the score value from the POST request
        current_user = request.user
        score = request.POST.get('score')
        goal = request.POST.get('goal')

        # Get the corresponding goal object
        try:
            current_goal = Goal.objects.get(name = goal)
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})

        daily_status = DailyData.complete_goal(current_user, current_goal)

        # Update the score if needed
        if (int(daily_status.score) < int(score)):
            daily_status.score = score
            daily_status.save()

        # Return a JSON response to indicate success
        return JsonResponse({'success': True})
    else:
        # Return an error response if the request is not valid
        return JsonResponse({'success': False, 'error': 'Invalid request'})

# Helpers

def get_completed_goals(user):
    """
    Get goals completed by the user on that day
    """

    # get user's completed goals
    today = datetime.date.today()
    try:
        daily_data = DailyData.objects.get(date=today, user=user)
        completed_goals = daily_data.daily_goals.filter(
            dailygoalstatus__completed=True)
        return completed_goals

    except DailyData.DoesNotExist:
        return []