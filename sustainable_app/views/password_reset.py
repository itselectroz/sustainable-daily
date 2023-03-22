
from django.shortcuts import redirect, render, reverse


def password_reset(request):
    """
    If the user is logged in, they may change their password
    """
    current_user = request.user

    # if the user is not logged in
    if not current_user.is_authenticated:
        return redirect(reverse('login'))

    # if the change password form was submitted
    if request.method != "POST" or request.POST is None:
        # render change password page
        return render(request, 'sustainable_app/password_reset.html', {
            'error': False
        })

    password = request.POST.get('password', '')
    new = request.POST.get('new', '')
    confirm = request.POST.get('confirm', '')

    # if user's password is incorrect, return error
    if not current_user.check_password(password):
        return render(request, 'sustainable_app/password_reset.html', {
            'errorAuth': True
        })

    # if passwords do not match, return error
    if new != confirm:
        return render(request, 'sustainable_app/password_reset.html', {
            'errorMatch': True
        })

    # set new password
    current_user.set_password(new)
    current_user.save()

    # return to home/game keeper page
    if (current_user.game_keeper):
        return redirect(reverse('game_keeper'))

    return redirect(reverse('home'))


def forgot_password(request):
    """
    If the user has forgotten their password, they may send
    an email to a game keeper to reset it
    """

    # render reset password page
    return render(request, 'sustainable_app/forgot_password.html', {
        'error': False
    })
