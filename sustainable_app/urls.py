from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='index'), # TODO: change this to home once the home view exists
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name="register"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
]
