from django.shortcuts import render


def register(request):
    return render(request, 'sustainable_app/register.html')
