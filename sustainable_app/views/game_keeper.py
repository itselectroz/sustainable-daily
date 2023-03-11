from django.shortcuts import render, redirect, reverse
from django.core.files import File

from io import BytesIO

from sustainable_app.models.user import User
from sustainable_app.models.location import Location
import qrcode

# game keeper page
def game_keeper(request):
    
    if request.method == "POST" and request.POST is not None:
        return locations_add(request)
    
    # send all game keepers to template
    context = {
        "game_keepers":  User.objects.filter(game_keeper=True)
    }
    
    return direct_user("", request, context) 
   
# game keeper locations page
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

# Remove keeper request
def remove_keeper(request):
    # get username from post request
    username = request.POST.get('username', False)
    # delete user with given username
    User.objects.get(username=username).delete()
    # refresh the page
    return redirect('/')

# add a location
def locations_add(request):
    if(request.user.is_authenticated and request.user.game_keeper):
        # if there is a post request
        if request.method == 'POST':
            # get location attributes from post request
            name = request.POST.get('name', '')
            category = request.POST.get('category', '')
            clue = request.POST.get('clue', '')
            image = request.POST.get('image', '')
            
            # create location object
            new_location = Location(name=name, category=category, clue=clue)
            new_location.save()
            
            # generate qr code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            
            #TODO: When deployed change data to url
            qr.add_data('127.0.0.1:8000/location_qr/' + str(new_location.id))
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            
            # set attributes
            new_location.image = request.FILES['image']
            new_location.qr.save(f"qr_{new_location.id}.png", File(buffer))
        
            return redirect(reverse('game_keeper_locations'))
        else:
            return redirect(reverse('home'))

# remove a location
def locations_remove(request):
    
    # if user is authenticated
    if(request.user.is_authenticated):
        # get location id from post request
        location_id = request.POST.get('location_id', False)
        # delete user with given username
        Location.objects.get(id=location_id).delete()
        # refresh the page
        return redirect(reverse('game_keeper_locations'))

# direct user to correct page
def direct_user(page, request, context):
    # if user is authenticated
    if(request.user.is_authenticated):
        # if user is a game keeper
        if(request.user.game_keeper):
            # render game keeper locations page
            return render(request, 'sustainable_app/game_keeper' + page + '.html', context)
        else:
            # render home page
            return redirect(reverse('home'))
    else:
        # render login
        return redirect(reverse('login'))
    

