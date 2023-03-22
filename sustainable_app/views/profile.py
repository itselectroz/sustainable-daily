from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy

from sustainable_app.models.user import Item
from sustainable_app.util import username_dict, background_dict


@login_required(login_url=reverse_lazy('login'))
def profile(request):
    """
    Renders profile with user data
    """

    current_user = request.user

    # get user attributes
    user_name_color = username_dict[str(
        current_user.equipped_items.get(type="username_color"))]
    background_color = background_dict[str(
        current_user.equipped_items.get(type="background_color"))]

    user_level = current_user.level()
    xp_to_level = current_user.xp_for_level(user_level + 1)

    user_accessory = current_user.equipped_items.get(type="accessory")
    user_character = current_user.equipped_items.get(type="character")

    # for dislaying point shop correctly
    all_characters = Item.objects.filter(type="character")

    purchasable_types = [
        "accessory", "username_color", "background_color"
    ]

    all_items = Item.objects.filter(type__in=purchasable_types)

    owned_items = current_user.owned_items.filter(type__in=purchasable_types)

    purchasable_items = set(all_items).difference(set(owned_items))

    # setting owned characters
    for character in all_characters:
        if character.unlock_level <= user_level:
            current_user.owned_items.add(character.id)

    # pass user attributes to template
    context = {"user": current_user,
               "text_color": user_name_color,
               "background_color": background_color,
               "user_level": user_level,
               "character": user_character,
               "accessory": user_accessory,
               "all_characters": all_characters,
               "purchasable_items": purchasable_items,
               "owned_items": owned_items,
               "xp_to_level": xp_to_level,
               }

    return render(request, "sustainable_app/profile.html", context)

# Equip request


def equip(request):
    """
    Equips item selected by user
    """

    current_user = request.user

    # Get the type and name of item
    type = request.POST.get('type', False)
    name = request.POST.get('name', False)

    # Pass to function
    changeAccessory(type, name, current_user)

    return HttpResponse(status=200)

# Change accessory


def changeAccessory(type, name, current_user):
    """
    If the user owns the item they are trying to equip,
    removes item of same type and equips new item
    """

    # check if item is owned
    exists = False
    for item_to_add in current_user.owned_items.all():
        if item_to_add.type == type and item_to_add.name == str(name):
            exists = True

    if (not exists):
        return HttpResponse('Object not found', status=404)

    # find item to remove and remove it
    for item_to_remove in current_user.equipped_items.all():
        if item_to_remove.type == type:
            current_user.equipped_items.remove(item_to_remove.id)

    # find item to add and add it
    for item_to_add in current_user.owned_items.all():
        if item_to_add.type == type and item_to_add.name == str(name):
            current_user.equipped_items.add(item_to_add.id)


def purchase(request):
    """
    Adds purchased item to user's owned items
    """
    current_user = request.user

    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    # Get the type and name of item
    type = request.POST.get('type', False)
    name = request.POST.get('name', False)

    try:
        purchased_item = Item.objects.get(type=type, name=name)
        current_user.owned_items.add(purchased_item.id)
        current_user.points -= purchased_item.cost
        current_user.save()
        return HttpResponse(status=200)

    except Item.DoesNotExist:
        return HttpResponse('Object not found', status=404)
