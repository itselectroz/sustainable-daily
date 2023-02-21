from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse

from sustainable_app.models.user import User


@login_required(login_url=reverse('login'))
def leaderboard(request): # TODO: write tests maybe?
    names = User.objects.order_by("-xp")

    return render(request, 'sustainable_app/leaderboard.html', {
        "names": names
    })
