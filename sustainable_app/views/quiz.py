from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from sustainable_app.models import QuizQuestion
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('login'))
def quiz(request):
    # Get up to 5 random questions
    questions = QuizQuestion.objects.order_by('?')[:5]

    questions = serializers.serialize('json', questions)

    context = {
        "questions":questions
    }

    return render(request, 'sustainable_app/quiz.html', context=context)
