from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sustainable_app.models.user import User



@login_required(login_url='/login')
def profile(request):

    template = loader.get_template("sustainable_app/profile.html")

    current_user = request.user
    current_user.equipped_items.add(1)

    # get user attributes
    user_name_color = current_user.equipped_items.get(type="username_color")

    # TODO: Caculate xp needed for next level

    user_level = current_user.level

    # user_background_color = current_user.equipped_items.get(type="background_color")
    # user_hat = current_user.equipped_items.get(type="hat")
    # user_character = current_user.equipped_items.get(type="character")

    # pass user attributes to template
    context = {"user": current_user,
               "text_color": user_name_color,
               "user_level":user_level,
               }

    return render(request, "sustainable_app/profile.html", context)
