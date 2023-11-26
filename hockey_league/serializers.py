from rest_framework import serializers

from .models import HockeyLeague, Team, Match, Ticket, TypeTicket, Player, Season, PlayerStatistic


class HockeyLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = HockeyLeague
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class TypeTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTicket
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class PlayerStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatistic
        fields = '__all__'
