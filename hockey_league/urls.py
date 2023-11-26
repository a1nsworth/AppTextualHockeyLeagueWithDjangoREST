from django.urls import path
from . import views

urlpatterns = [
    path("hockey_league/", views.HockeyLeagueListView.as_view()),
    path("hockey_league/<str:pk>", views.HockeyLeagueDetailsView.as_view()),
]
