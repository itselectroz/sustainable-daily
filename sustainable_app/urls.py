from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name="home"),
    path('home/complete_personal/', views.complete_personal, name="complete_personal"),
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
    path('game_keeper/locations_add/', views.locations_add, name="locations_add"),
    path('game_keeper/locations_remove/', views.locations_remove, name="locations_remove"),
    path('game_keeper/open/<int:goal_id>/', views.open_file, name='open-file'),
    path('game_keeper_locations/', views.game_keeper_locations, name="game_keeper_locations"),
    path('game_keeper_surveys/', views.game_keeper_surveys, name="game_keeper_surveys"),
    path('game_keeper_events/', views.game_keeper_events, name="game_keeper_events"),
    path('location_qr/<int:id>/', views.qr_callback, name="qr_callback"),
    path('password_reset/', views.password_reset, name="password_reset"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('quiz/', views.quiz, name="quiz"),
    path('minigame_survey/', views.minigame_survey, name="minigame_survey"),
]
