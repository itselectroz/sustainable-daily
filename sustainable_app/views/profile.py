from django.shortcuts import render


def profile(request):
    return render(request, 'sustainable_app/profile.html')
