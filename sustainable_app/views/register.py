from django.shortcuts import render, redirect, reverse


def register(request):
    if request.user.is_authenticated:
        # TODO: change this to home when home page is done
        return redirect(reverse('profile'))

    return render(request, 'sustainable_app/register.html')
