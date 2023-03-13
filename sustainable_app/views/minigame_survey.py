from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Prefetch
from django.shortcuts import redirect

from sustainable_app.models.survey import Question,Choice

@login_required(login_url='/login')
def minigame_survey(request):

    questions = Question.objects.order_by("pub_date")
    questions = Question.objects.prefetch_related(Prefetch('choice_set', queryset=Choice.objects.order_by('choice_text')))
    choices = Choice.objects.all()
    context = {'questions': questions, 'choices' : choices}

    if request.method == 'POST':

        strings_to_exclude = ('csrfmiddlewaretoken', 'survey-submit')

        filtered_keys = [key for key in request.POST.keys() if key not in strings_to_exclude]

        #Gets choice entry and adds to votes
        for q_id in filtered_keys:
            #Gets the id of the choice that needs to be added to
            choice_id_to_change = request.POST.get(q_id)

            choice = Choice.objects.get(id = choice_id_to_change)

            choice.votes +=1
            choice.save()

        return redirect('home')


    return render(request, 'sustainable_app/minigame_survey.html', context)


