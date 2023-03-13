from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from sustainable_app.models.user import Item
from sustainable_app.util import username_dict, background_dict


@login_required(login_url=reverse_lazy('login'))
def profile(request):

    current_user = request.user

    # get user attributes
    user_name_color = username_dict[str(
        current_user.equipped_items.get(type="username_color"))]
    background_color = background_dict[str(
        current_user.equipped_items.get(type="background_color"))]

    # TODO: Caculate xp needed for next level

    user_level = current_user.level

    # user_background_color = current_user.equipped_items.get(type="background_color")
    user_accessory = current_user.equipped_items.get(type="accessory")
    user_character = current_user.equipped_items.get(type="character")
    
    all_characters = Item.objects.filter(type="character")

    # pass user attributes to template
    context = {"user": current_user,
               "text_color": user_name_color,
               "background_color": background_color,
               "user_level": user_level,
               "character": user_character,
               "accessory": user_accessory,
               "all_characters": all_characters,
               }

    return render(request, "sustainable_app/profile.html", context)

# Equip request


def equip(request):

    current_user = request.user

    # Get the type and name of item
    # TODO: Change type to diff variable name
    type = request.POST.get('type', False)
    name = request.POST.get('name', False)

    # Pass to function
    changeAccessory(type, name, current_user)

    return HttpResponse(status=200)

# Change accessory


def changeAccessory(type, name, current_user):
    # TODO: check if the user owns the accessory
    # we currently do not have "owned_items" implemented

    

    # check if item is owned
    exists = False
    for item_to_add in current_user.owned_items.all():
        if item_to_add.type == type and item_to_add.name == str(name):
            exists = True

    if(exists == False):
        return Item.DoesNotExist
    
    # find item to remove and remove it
    for item_to_remove in current_user.equipped_items.all():
        if item_to_remove.type == type:
            current_user.equipped_items.remove(item_to_remove.id)
            
    # find item to add and add it
    for item_to_add in current_user.owned_items.all():
        if item_to_add.type == type and item_to_add.name == str(name):
            current_user.equipped_items.add(item_to_add.id)
    
