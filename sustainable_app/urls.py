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
    path('sorting/', views.sorting, name='sorting'),
    path('minigame_catching/', views.minigame_catching, name="minigame_catching"),
    path('game_keeper/', views.game_keeper, name="game_keeper"),
    path('game_keeper/remove_keeper/', views.remove_keeper, name="remove_keeper"),
    path('game_keeper_locations/', views.game_keeper_locations, name="game_keeper_locations"),
    path('game_keeper_surveys/', views.game_keeper_surveys, name="game_keeper_surveys"),
    path('game_keeper_events/', views.game_keeper_events, name="game_keeper_events"),
]
