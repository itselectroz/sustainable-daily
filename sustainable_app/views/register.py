from django.db import IntegrityError
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login

from ..models import User, Item


def register_user(request):
    """
    Registers user, creates user object and redirects
    according to ther user's type
    """
    issues = []

    # Check all fields are present and note down those that aren't
    for name in ['username', 'password', 'first-name', 'last-name', 'email']:
        if not request.POST.get(name, ''):
            issues.append(name)

    if len(issues) > 0:
        return render(request, 'sustainable_app/register.html', {
            'error': True,
            'error_message': 'Missing required information.',
            'issues': issues
        })

    # get user attributes from post request
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    first_name = request.POST.get('first-name', '')
    last_name = request.POST.get('last-name', '')
    email = request.POST.get('email', '')
    is_admin = request.POST.get('admin', '')

    if len(password) < 6:
        return render(request, 'sustainable_app/register.html', {
            'error': True,
            'error_message': 'Password must be at least 6 characters long.',
            'issues': []
        })

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

    # if user is authenticated, is a game keeper,
    # and wants to create a game keeper
    if (is_admin and request.user.is_authenticated
            and request.user.game_keeper):
        # set user game_keeper attribute to true
        user.game_keeper = True

    # Set default equipped items so it doesn't break
    default_items = ['badger', 'none', 'u_black', 'b_white']
    for item_name in default_items:
        try:
            item = Item.objects.get(name=item_name)
            user.owned_items.add(item.id)
            user.equipped_items.add(item.id)
        except Item.DoesNotExist:
            return render(request, 'sustainable_app/register.html', {
                'error': True,
                'error_message': 'Something went wrong, please try again.',
                'issues': []
            })

    # Commit user to database
    user.save()

    # Login the user to streamline process
    if (not is_admin):
        login(request, user)

    # if game keeper then direct to game keeper page, else direct to home
    if (is_admin):
        return redirect(reverse('game_keeper'))
    else:
        return redirect(reverse('home'))


def register(request):
    """
    Handles registration request
    """
    if request.user.is_authenticated and not request.user.game_keeper:
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

    is_admin = request.user.is_authenticated and request.user.game_keeper

    return render(request, 'sustainable_app/register.html', {
        'error': False,
        'issues': [],
        'isAdmin': is_admin,
    })


def privacy_policy(request):
    """
    Renders privacy policy
    """
    # No authentication checks on this page
    # It's fine for an authenticated user to see the privacy policy.

    return render(request, 'sustainable_app/privacy_policy.html', {})
