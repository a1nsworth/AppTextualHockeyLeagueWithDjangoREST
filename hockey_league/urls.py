from rest_framework import routers
from django.urls import path, include

from . import views
from .routers_creator import SimpleRouterCreator

urlpatterns = [
    path('', include(SimpleRouterCreator(r'hockey_league', views.HockeyLeagueReadOnlyViewSet).urls)),
    path('', include(SimpleRouterCreator(r'season', views.SeasonViewSet).urls)),
    path('', include(SimpleRouterCreator(r'player', views.PlayerViewSet).urls)),
    path('', include(SimpleRouterCreator(r'player_stat', views.PlayerStatisticViewSet).urls)),
    path('', include(SimpleRouterCreator(r'type_ticket', views.TypeTicketViewSet).urls)),
    path('', include(SimpleRouterCreator(r'ticket', views.TicketViewSet).urls)),
    path('', include(SimpleRouterCreator(r'match', views.MatchViewSet).urls)),
    path('', include(SimpleRouterCreator(r'team', views.TeamViewSet).urls)),
]
