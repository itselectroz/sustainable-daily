from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

from sustainable_app.models.user import User


@login_required(login_url=reverse_lazy('login'))
def leaderboard(request):  # TODO: write tests maybe?
    names = User.objects.order_by("-xp")

    return render(request, 'sustainable_app/leaderboard.html', {
        "names": names
    })
