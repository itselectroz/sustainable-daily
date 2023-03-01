from django.db import IntegrityError
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login

from ..models import User


def register_user(request):
    issues = []

    # Check all fields are present and note down those that aren't
    for name in ['username', 'password', 'first-name', 'last-name', 'email']:
        if not request.POST.get(name, ''):
            issues.append(name)

    if len(issues) > 0:
        # TODO: once register view has been themeified by oscar, this error stuff needs to be reimplemented
        return render(request, 'sustainable_app/register.html', {
            'error': True,
            'error_message': 'Missing required information.',
            'issues': issues
        })

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    first_name = request.POST.get('first-name', '')
    last_name = request.POST.get('last-name', '')
    email = request.POST.get('email', '')

    try:
        # Create user object
        user = User.objects.create_user(username, email, password)
    except IntegrityError:
        return render(request, 'sustainable_app/register.html', {
            'error': True,
            'error_message': 'Account with username already exists.',
            'issues': []
        })

    user.first_name = first_name
    user.last_name = last_name

    # Set default equipped items so it doesn't break
    user.equipped_items.add(1)
    user.equipped_items.add(10)
    user.equipped_items.add(20)
    user.equipped_items.add(30)

    # Commit user to database
    user.save()

    # Login the user to streamline process
    login(request, user)

    return redirect(reverse('home'))


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST" and request.POST is not None:
        try:
            return register_user(request)
        except Exception:
            return render(request, 'sustainable_app/register.html', {
                'error': True,
                'error_message': 'Something went wrong, please try again.',
                'issues': []
            })

    return render(request, 'sustainable_app/register.html', {
        'error': False,
        'issues': []
    })
