from django.shortcuts import render, redirect, reverse
from django.core.files import File
from django.http import FileResponse, HttpResponse


from io import BytesIO

from sustainable_app.models import User, Location, Goal, DailyData
import qrcode
# game keeper page


def game_keeper(request):
    if request.method == "POST" and request.POST is not None:
        return locations_add(request)
    

    # send all game keepers to template
    context = {
        "game_keepers":  User.objects.filter(game_keeper=True),
        "current_keeper_id": request.user.id,
    }

    return direct_user("", request, context)


def game_keeper_locations(request):
    # send all locations to template
    context = {
        "locations":  Location.objects.all()
    }
    return direct_user("_locations", request, context)


def game_keeper_surveys(request):
    return direct_user("_surveys", request, {})


def game_keeper_events(request):
    return direct_user("_events", request, {})


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

# add a location


def locations_add(request):
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
    new_goal = Goal.objects.create(name=name, description="",  type=Goal.LOCATION, point_reward=100, xp_reward=100)
    
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

    # TODO: When deployed change data to url
    qr.add_data('127.0.0.1:8000/location_qr/' + str(new_goal.id))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format='PNG')

    # set attributes
    new_location.image = request.FILES['image']
    new_location.qr.save(f"qr_{new_location.id}.png", File(buffer))

    return redirect(reverse('game_keeper_locations'))

# remove a location


def locations_remove(request):
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

def qr_callback(request, id):
    if(not request.user.is_authenticated):
        return HttpResponse('Forbidden', status=403)
    
    try:
        goal = Goal.objects.get(id=id)
    except Goal.DoesNotExist:
        return HttpResponse('Object not found', status=404)
    
    
    DailyData.complete_goal(request.user, goal)
    
    # TODO: Success page
    return HttpResponse('Goal completed successfully', status=200)


def open_file(request, goal_id):
    """
    User may download the qr code as a png file, to then print and put somewhere on campus
    """
    
    try:
        goal = Goal.objects.get(id=goal_id)
        location = Location.objects.get(goal=goal)
    except Goal.DoesNotExist:
        return HttpResponse('Object not found', status=404)
    
    filename = "qrcode_" + location.name + ".png"
    
    return FileResponse(location.qr.open(), as_attachment=True, filename=filename)
