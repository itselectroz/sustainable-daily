from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.core import serializers

from sustainable_app.models import (
    SurveyQuestion, SurveyChoice, Survey,
    Goal, DailyData, QuizQuestion
)


@login_required(login_url=reverse_lazy('login'))
def quiz(request):
    """
    Gets quiz questions and renders the quiz
    """

    # Get up to 5 random questions
    questions = QuizQuestion.objects.order_by('?')[:5]

    # Completing this goal for user
    user = request.user
    goal = Goal.objects.get(type=Goal.QUIZ)
    DailyData.complete_goal(user, goal)

    questions = serializers.serialize('json', questions)

    context = {
        "questions": questions
    }

    return render(request, 'sustainable_app/quiz.html', context=context)


@login_required(login_url=reverse_lazy('login'))
def survey(request, id):
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


@login_required(login_url=reverse_lazy('login'))
def minigame_catching(request):
    """
    Renders catching minigame
    """
    return render(request, 'sustainable_app/minigame_catching.html')


@login_required(login_url=reverse_lazy('login'))
def minigame_sorting(request):
    """
    Renders sorting minigame
    """
    return render(request, 'sustainable_app/sorting.html')
