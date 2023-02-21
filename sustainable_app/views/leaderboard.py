from django.http import HttpResponse
from django.template import loader

from sustainable_app.models.user import User


def leaderboard(request):

    template = loader.get_template("sustainable_app/leaderboard.html")

    # Figure out how to get names for leaderboard
    names = User.objects.order_by("-xp")
    context = {"names": names}
    return HttpResponse(template.render(context))
