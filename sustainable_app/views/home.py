from django.shortcuts import render


def home(request):
    return render(request, 'sustainable_app/home.html')
