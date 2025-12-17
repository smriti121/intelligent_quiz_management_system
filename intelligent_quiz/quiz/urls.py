# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ---------------- Home ----------------
    path('', views.home, name='home'),

    # ---------------- Authentication ----------------
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # ---------------- Profile ----------------
    path('profile/', views.profile, name='profile'),

    # ---------------- Quiz ----------------
    path('start/', views.start_quiz, name='start_quiz'),

    # ---------------- Leaderboard ----------------
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
