from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse_lazy
from sustainable_app.models import Question

@login_required(login_url=reverse_lazy('login'))
def quiz(request):
    # Get up to 5 random questions
    questions = Question.objects.order_by('?')[:5]

    questions = serializers.serialize('json', questions)

    context = {
        "questions":questions
    }

    return render(request, 'sustainable_app/quiz.html', context=context)
