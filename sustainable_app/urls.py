from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name="home"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name="profile"),
    path('profile/equip/', views.equip, name="equip"),
    path('register/', views.register, name="register"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path(
        'minigame_catching/', views.minigame_catching,
        name="minigame_catching"
    ),
]
