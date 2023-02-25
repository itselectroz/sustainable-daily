from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sustainable_app.models.user import User, Item



@login_required(login_url='/login')
def profile(request):

    template = loader.get_template("sustainable_app/profile.html")

    current_user = request.user

    # get user attributes
    user_name_color = current_user.equipped_items.get(type="username_color")
    background_color = current_user.equipped_items.get(type="background_color")

    # TODO: Caculate xp needed for next level

    user_level = current_user.level

    # user_background_color = current_user.equipped_items.get(type="background_color")
    # user_hat = current_user.equipped_items.get(type="hat")
    # user_character = current_user.equipped_items.get(type="character")

    # pass user attributes to template
    context = {"user": current_user,
               "text_color": user_name_color,
               "background_color": background_color,
               "user_level":user_level,
               }

    return render(request, "sustainable_app/profile.html", context)

# Equip request
def equip(request):

    current_user = request.user

    # Get the type and name of item
    type = request.POST.get('type', False)
    name = request.POST.get('name', False)

    # Pass to function
    changeAccessory(type, name, current_user)

    return redirect('/')

# Change accessory
def changeAccessory(type, name, current_user):
    
    ## find item to remove and remove it
    for item_to_remove in Item.objects.all():
        if item_to_remove.type == type:
            current_user.equipped_items.remove(item_to_remove.id)

    ## find item to add and add it
    for item_to_add in Item.objects.all():
        if item_to_add.type == type:
            if item_to_add.name == str(name):
                current_user.equipped_items.add(item_to_add.id)