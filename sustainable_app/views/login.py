from django.shortcuts import render


def login(request):
    return render(request, 'sustainable_app/login.html')
