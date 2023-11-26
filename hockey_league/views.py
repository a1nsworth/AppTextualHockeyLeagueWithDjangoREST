from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import HockeyLeague
from .serializers import HockeyLeagueSerializer


class HockeyLeagueListView(ListAPIView):
    """Вывод всех хоккейных лиг"""

    queryset = HockeyLeague.objects.all()
    serializer_class = HockeyLeagueSerializer


class HockeyLeagueDetailsView(RetrieveAPIView):
    queryset = HockeyLeague.objects.all()
    serializer_class = HockeyLeagueSerializer
