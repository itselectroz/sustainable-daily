from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#@login_required(login_url='/login')
def quiz(request):
    return render(request, 'sustainable_app/quiz.html')
