from rest_framework import serializers

from .models import HockeyLeague


class HockeyLeagueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HockeyLeague
        field = ('name',)
