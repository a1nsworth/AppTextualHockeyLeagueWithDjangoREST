from rest_framework.response import Response
from rest_framework.views import APIView

from .models import HockeyLeague
from .serializers import HockeyLeagueListSerializer


class HockeyLeagueListView(APIView):
    """Вывод всех хоккейных лиг"""

    def get(self, request):

        hockey_league = HockeyLeague.objects.all()
        serializer = HockeyLeagueListSerializer(hockey_league, many=True)
        return Response(serializer.data)
