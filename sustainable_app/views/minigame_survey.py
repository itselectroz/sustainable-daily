from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Prefetch
from django.http import HttpResponse

from sustainable_app.models.survey import Question,Choice

#@login_required(login_url='/login')
def minigame_survey(request):

    questions = Question.objects.order_by("pub_date")
    questions = Question.objects.prefetch_related(Prefetch('choice_set', queryset=Choice.objects.order_by('choice_text')))
    choices = Choice.objects.all()
    context = {'questions': questions, 'choices' : choices}


    return render(request, 'sustainable_app/minigame_survey.html', context)


def temp(request):
    if request.method == 'POST':

        question_ids = [key for key in request.POST.keys() if key != 'csrfmiddlewaretoken']

        #Gets choice entry and adds to votes
        for question in question_ids:
            #Gets the id of the choice that needs to be added to
            choice_id_to_change = request.POST.get(question_ids[question])

            choice = Choice.objects.get(choice_id = choice_id_to_change)

            choice.votes +=1
            choice.save()

        return render("Hello")
