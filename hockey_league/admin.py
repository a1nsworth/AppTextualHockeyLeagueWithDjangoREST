from django.contrib import admin
from .models import HockeyLeague, Season, Team, Player, PlayerStatistic, Ticket, TypeTicket, CashMachine, Match

admin.site.register(HockeyLeague)
admin.site.register(Season)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayerStatistic)
admin.site.register(Match)
admin.site.register(CashMachine)
admin.site.register(Ticket)
admin.site.register(TypeTicket)
