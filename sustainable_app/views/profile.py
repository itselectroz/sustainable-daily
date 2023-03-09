from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from sustainable_app.models.user import Item

# Dictionaries

background_dict = {
    "b_green": "#65d982",
    "b_grey": "#858186",
    "b_pink": "#dd69e7",
    "b_blue": "#17a3c9",
    "b_white": "#ffffff",
}

username_dict = {
    "u_green": "#14820a",
    "u_black": "#000000",
    "u_purple": "#5f0b7b",
    "u_blue": "#192e6c",
    "u_orange": "#ed8114",
}


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

    # pass user attributes to template
    context = {"user": current_user,
               "text_color": user_name_color,
               "background_color": background_color,
               "user_level": user_level,
               "character": user_character,
               "accessory": user_accessory,
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

    # find item to remove and remove it
    for item_to_remove in current_user.equipped_items.all():
        if item_to_remove.type == type:
            current_user.equipped_items.remove(item_to_remove.id)

    # find item to add and add it
    for item_to_add in Item.objects.all():
        if item_to_add.type == type and item_to_add.name == str(name):
            current_user.equipped_items.add(item_to_add.id)
