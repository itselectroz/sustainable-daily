from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse_lazy

from sustainable_app.models import QuizQuestion, DailyData, Goal


@login_required(login_url=reverse_lazy('login'))
def quiz(request):
    # Get up to 5 random questions
    questions = QuizQuestion.objects.order_by('?')[:5]

    # Completing this goal for user
    user = request.user
    goal = Goal.objects.get(name="quiz")
    DailyData.complete_goal(user, goal)

    questions = serializers.serialize('json', questions)

    context = {
        "questions": questions
    }

    return render(request, 'sustainable_app/quiz.html', context=context)
