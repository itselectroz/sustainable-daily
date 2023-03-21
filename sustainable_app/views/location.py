from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

from sustainable_app.models import Goal, Location, DailyData, Statistics

location_types = {
    'recycle': 'Recycling Bin',
    'water': 'Water Fountain'
}

@login_required(login_url=reverse_lazy('login'))
def view_location(request, id):
    goal = get_object_or_404(Goal, id=id)
    location = get_object_or_404(Location, goal=goal)

    return render(request, 'sustainable_app/view_location.html', {
        'location': location,
        'type': location_types[location.category]
    })

def qr_callback(request, id):
    if (not request.user.is_authenticated):
        return HttpResponseForbidden()

    goal = get_object_or_404(Goal, id=id)

    DailyData.complete_goal(request.user, goal)

    location = get_object_or_404(Location, goal=goal)
    if location.category == location.RECYCLE:
        Statistics.increment_quantity("plastic")
    if location.category == location.WATER:
        Statistics.increment_quantity("water")

    # Success page
    return render(request, 'sustainable_app/qr_complete.html')
