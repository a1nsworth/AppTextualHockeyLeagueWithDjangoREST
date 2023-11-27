from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import HockeyLeague, Season, Player, PlayerStatistic, TypeTicket, Ticket, Team, Match, CashMachine
from .serializers import HockeyLeagueSerializer, SeasonSerializer, PlayerSerializer, \
    PlayerStatisticSerializer, TicketSerializer, MatchSerializer, TeamSerializer, TypeTicketSerializer, \
    CashMachineSerializer


class HockeyLeagueReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = HockeyLeague.objects.all()
    serializer_class = HockeyLeagueSerializer


class SeasonViewSet(ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerStatisticViewSet(ModelViewSet):
    queryset = PlayerStatistic.objects.all()
    serializer_class = PlayerStatisticSerializer


class TypeTicketViewSet(ModelViewSet):
    queryset = TypeTicket.objects.all()
    serializer_class = TypeTicketSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CashMachineReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = CashMachine.objects.all()
    serializer_class = CashMachineSerializer
