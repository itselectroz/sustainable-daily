from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from sustainable_app.models import Goal, Location

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
