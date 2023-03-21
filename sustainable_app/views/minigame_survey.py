from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from sustainable_app.models import SurveyQuestion, SurveyChoice, Survey, Goal, DailyData


@login_required(login_url=reverse_lazy('login'))
def minigame_survey(request, id):
    """
    Renders survey
    """
    goal = get_object_or_404(Goal, id=id)
    active_survey = get_object_or_404(Survey, goal=goal)
    questions = SurveyQuestion.objects.filter(survey=active_survey)
    choices = SurveyChoice.objects.filter(question__in=questions)
    context = {'questions': questions, 'choices': choices}

    if request.method == 'POST':

        strings_to_exclude = ('csrfmiddlewaretoken', 'survey-submit')

        filtered_keys = [key for key in request.POST.keys()
                         if key not in strings_to_exclude]

        # Gets choice entry and adds to votes
        for q_id in filtered_keys:
            # Gets the id of the choice that needs to be added to
            choice_id_to_change = request.POST.get(q_id)

            try:
                choice = SurveyChoice.objects.get(id=choice_id_to_change)

                choice.votes += 1
                choice.save()
            except SurveyChoice.DoesNotExist:
                return HttpResponseBadRequest()

        # Complete goal
        DailyData.complete_goal(request.user, goal)

        return redirect('home')

    return render(request, 'sustainable_app/minigame_survey.html', context)
