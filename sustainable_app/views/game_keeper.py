from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.files import File
from django.http import FileResponse, HttpResponse

from io import BytesIO

from sustainable_app.models import User, Location, Goal, DailyData, QuizQuestion, Survey, SurveyQuestion, SurveyChoice, Statistics
import qrcode
import datetime

# game keeper page


def game_keeper(request):
    """
    Handles game keeper requests and sends game keepers and stats to template
    """
    if request.method == "POST" and request.POST is not None:
        return locations_add(request)

    # get statistics
    stats = Statistics.objects.all()
    plastic_stat = stats.get(name='plastic')
    recycle_stat = stats.get(name='water')

    # serialise gamekeepers
    game_keepers = []
    for user in User.objects.filter(game_keeper=True):
        game_keepers.append({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        })

    # send all game keepers to template
    context = {
        "game_keepers":  User.objects.filter(game_keeper=True),
        "current_keeper_id": request.user.id,
        "plastic": plastic_stat,
        "water": recycle_stat,
    }

    return direct_user("", request, context)


def game_keeper_locations(request):
    """
    Handles game keeper locations requests
    """
    # request to add location
    if request.method == "POST" and request.POST is not None:
        return locations_add(request)

    # send all locations to template
    context = {
        "locations":  Location.objects.all()
    }
    return direct_user("_locations", request, context)


def game_keeper_surveys(request):
    """
    Handles game keeper survyes requests
    """
    # request to add survey
    if request.method == "POST" and request.POST is not None:
        if request.POST.get("form-type") == "create-survey":
            return surveys_add(request)
        if request.POST.get("form-type") == "create-question":
            return surveys_question_add(request)

    # send all surveys to template
    context = {
        "surveys":  Survey.objects.all(),
        "questions": SurveyQuestion.objects.all(),
        "choices": SurveyChoice.objects.all(),
    }

    return direct_user("_surveys", request, context)


def game_keeper_questions(request):
    """
    Handles game keeper questions requests
    """
    # request to add question
    if request.method == "POST" and request.POST is not None:
        return questions_add(request)

    # send all quiz questions to template
    context = {
        "questions":  QuizQuestion.objects.all()
    }

    # questions template
    return direct_user("_questions", request, context)


def remove_keeper(request):
    """
    View for removing a game keeper
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    # get username from post request
    username = request.POST.get('username', False)
    # delete user with given username
    User.objects.get(username=username).delete()
    # refresh the page
    return redirect('/')



def locations_add(request):
    """
    Adds a location if the user is authorized
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    if (request.method != 'POST'):
        # redirect to home if it's not a post request
        return redirect(reverse('home'))

    # get location attributes from post request
    name = request.POST.get('name', '')
    category = request.POST.get('category', '')
    clue = request.POST.get('clue', '')

    # create a goal
    new_goal = Goal.objects.create(
        name=name,
        description="",
        type=Goal.LOCATION,
        point_reward=100,
        xp_reward=100,
        image=f"sustainable_app/img/location_{category}.png",
    )

    new_goal.url = reverse('view_location', kwargs={'id': new_goal.id})

    new_goal.save()

    # create location object
    new_location = Location(name=name, category=category, clue=clue)
    new_location.goal = new_goal
    new_location.save()

    # generate qr code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(request.build_absolute_uri(
        reverse('qr_callback', kwargs={
            'id': new_goal.id
        })
    ))

    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format='PNG')

    # set attributes
    new_location.image = request.FILES['image']
    new_location.qr.save(f"qr_{new_location.id}.png", File(buffer))

    return redirect(reverse('game_keeper_locations'))



def locations_remove(request):
    """
    Removes a location if the user is authorized
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    # get location id from post request
    location_id = request.POST.get('location_id', False)
    # delete location image and qr
    remove_location = Location.objects.get(id=location_id)
    remove_goal = remove_location.goal
    try:
        remove_location.image.delete()
        remove_location.qr.delete()
    except Exception:
        pass

    # delete location with given id
    remove_location.delete()

    # delete the goal linked to the location
    remove_goal.delete()

    # refresh the page
    return redirect(reverse('game_keeper_locations'))



def surveys_add(request):
    """
    Creates a survey if user is authorized
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    if (request.method != 'POST'):
        # redirect to home if it's not a post request
        return redirect(reverse('home'))

    # get survey attributes from post request
    survey_text = request.POST.get('name', '')

    # create a goal
    new_goal = Goal.objects.create(
        name=survey_text,
        description="",
        type=Goal.MINIGAME,
        point_reward=100,
        xp_reward=100,
        image="sustainable_app/img/survey_image.png",
    )

    new_goal.url = reverse('survey', kwargs={'id': new_goal.id})
    new_goal.save()

    # create survey object
    new_survey = Survey(survey_text=survey_text, goal=new_goal)
    new_survey.save()

    return redirect(reverse('game_keeper_surveys'))



def surveys_remove(request):
    """
    Removes a survey question if the user is authorized
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    # get survey id from post request
    survey_id = request.POST.get('survey_id', False)

    remove_survey = Survey.objects.get(id=survey_id)

    # for all questions
    for question in SurveyQuestion.objects.all():
        # if question is part of survey
        if question.survey == remove_survey:
            # for all choices
            for choice in SurveyChoice.objects.all():
                # if choice is part of question
                if choice.question == question:
                    # delete choice
                    choice.delete()
            # delete question
            question.delete()

    # delete survey
    remove_survey.delete()

    # refresh the page
    return redirect(reverse('game_keeper_surveys'))



def surveys_question_add(request):
    """
    Creates a survey question if the user is authorized
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    if (request.method != 'POST'):
        # redirect to home if it's not a post request
        return redirect(reverse('home'))

    # get question attributes from post request
    question_text = request.POST.get('name', '')
    o1 = request.POST.get('o1', '')
    o2 = request.POST.get('o2', '')
    o3 = request.POST.get('o3', '')
    o4 = request.POST.get('o4', '')
    survey_id = int(request.POST.get('survey_selection', ''))

    try:
        survey = Survey.objects.get(id=survey_id)
    except Survey.DoesNotExist:
        return HttpResponse('Object not found', status=404)

    # create question object
    new_survey_question = SurveyQuestion(
        survey=survey, question_text=question_text, pub_date=datetime.datetime.now())
    new_survey_question.save()

    # create choices objects
    choices = [o1, o2, o3, o4]
    count = 0

    for choice in choices:
        if choice != '':
            count += 1

    for i in range(count):
        new_choice = SurveyChoice(
            question=new_survey_question, choice_text=choices[i])
        new_choice.save()

    return redirect(reverse('game_keeper_surveys'))



def questions_add(request):
    """
    Creates a question if the user is authorized
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    if (request.method != 'POST'):
        # redirect to home if it's not a post request
        return redirect(reverse('home'))

    # get question attributes from post request
    question = request.POST.get('question', '')
    a1 = request.POST.get('a1', '')
    a2 = request.POST.get('a2', '')
    a3 = request.POST.get('a3', '')
    a4 = request.POST.get('a4', '')
    correct_answer = int(request.POST.get('correct_select', ''))

    # create question object
    new_question = QuizQuestion(
        question=question, a1=a1, a2=a2, a3=a3, a4=a4, correct_answer=correct_answer)
    new_question.save()

    return redirect(reverse('game_keeper_questions'))



def questions_remove(request):
    """
    Deletes a question if the user is authorized
    """
    if (not request.user.is_authenticated or not request.user.game_keeper):
        return HttpResponse('Unauthorized', status=401)

    # get question id from post request
    question_id = request.POST.get('question_id', False)

    # delete question
    try:
        remove_question = QuizQuestion.objects.get(id=question_id)
    except QuizQuestion.DoesNotExist:
        return HttpResponse('Object not found', status=404)

    # delete question with given id
    remove_question.delete()

    # refresh the page
    return redirect(reverse('game_keeper_questions'))



def direct_user(page, request, context):
    """
    Function for directing user to correct page
    based on authentication and authorization
    """
    # if user is authenticated
    if (not request.user.is_authenticated):
        # redirect to login
        return redirect(reverse('login'))

    # if user is not a game keeper
    if (not request.user.game_keeper):
        # redirect to home page
        return redirect(reverse('home'))

    # render game keeper locations page
    return render(request, 'sustainable_app/game_keeper' + page + '.html', context)


def open_file(request, location_id):
    """
    User may download the qr code as a png file, to then print and put somewhere on campus
    """

    try:
        location = Location.objects.get(id=location_id)
    except Location.DoesNotExist:
        return HttpResponse('Object not found', status=404)

    filename = "qrcode_" + location.name + ".png"

    return FileResponse(location.qr.open(), as_attachment=True, filename=filename)
