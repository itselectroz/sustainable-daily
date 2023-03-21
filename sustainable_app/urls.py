from django.urls import path

from . import views

# List of URLs for navigating the app
urlpatterns = [
    path('', views.home, name="home"),
    path('complete_personal/', views.complete_personal, name="complete_personal"),
    path('update_recycle/', views.update_recycle, name='update_recycle'),
    path('update_water/', views.update_water, name='update_water'),
    path('update_daily_goal_status/',views.update_daily_goal_status, name='update_daily_goal_status'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name="profile"),
    path('profile/equip/', views.equip, name="equip"),
    path('profile/purchase/', views.purchase, name="purchase"),
    path('register/', views.register, name="register"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path('sorting/', views.sorting, name='sorting'),
    path('minigame_catching/', views.minigame_catching, name="minigame_catching"),
    path('game_keeper/', views.game_keeper, name="game_keeper"),
    path('game_keeper/remove_keeper/', views.remove_keeper, name="remove_keeper"),
    path('game_keeper/locations_remove/', views.locations_remove, name="locations_remove"),
    path('game_keeper/questions_remove/', views.questions_remove, name="questions_remove"),
    path('game_keeper/surveys_remove/', views.surveys_remove, name="surveys_remove"),
    path('game_keeper/open/<int:location_id>/', views.open_file, name='open-file'),
    path('game_keeper_locations/', views.game_keeper_locations, name="game_keeper_locations"),
    path('game_keeper_surveys/', views.game_keeper_surveys, name="game_keeper_surveys"),
    path('game_keeper_questions/', views.game_keeper_questions, name="game_keeper_questions"),
    path('location_qr/<int:id>/', views.qr_callback, name="qr_callback"),
    path('password_reset/', views.password_reset, name="password_reset"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('quiz/', views.quiz, name="quiz"),
    path('minigame_survey/<int:id>/', views.minigame_survey, name="minigame_survey"),
    path('view_location/<int:id>/', views.view_location, name="view_location"),
    path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
]
