from django.db import models
from django.core.validators import RegexValidator


# TODO спеки

class HockeyLeague(models.Model):
    """
    Модель Хоккейная Лига

    Атрибуты:
        name: название лиги
    """

    name = models.CharField(max_length=30, primary_key=True)


class Season(models.Model):
    """
    Модель Сезон

    Атрибуты:
        date_begin: дата начала сезона
        date_end: дата конца сезона
        hockey_league_name: название лиги
    """

    date_begin = models.DateField()
    date_end = models.DateField()
    hockey_league_name = models.ForeignKey(HockeyLeague, on_delete=models.SET_NULL, on_update=models.CASCADE)


class Team(models.Model):
    """
    Модель
    """

    name = models.CharField(max_length=30, primary_key=True)
    popularity = models.FloatField()
    season_id = models.ForeignKey(Season, on_delete=models.SET_NULL, on_update=models.CASCADE)


class Match(models.Model):
    """

    """

    location = models.CharField(max_length=50)
    date_time_start = models.DateTimeField()
    spend_money = models.FloatField()
    opponent_team_id_1 = models.ForeignKey(Team, on_delete=models.SET_NULL, on_update=models.CASCADE)
    opponent_team_id_2 = models.ForeignKey(Team, on_delete=models.SET_NULL, on_update=models.CASCADE)


class Player(models.Model):
    """
    """

    class Position(models.TextChoices):
        FORWARD = "FORWARD"
        DEFENSE = "DEFENSE"
        GOALIE = "GOALIE"

    NAME_VALIDATOR = RegexValidator(
        regex='^[А-Я][а-я]{1,}$',
        message='Имя должно содержать только буквы русского алфавита и начинаться с Заглавной буквы.',
        code='invalid_name',
    )

    first_name = models.CharField(max_length=50, validators=[NAME_VALIDATOR])
    second_name = models.CharField(max_length=50, validators=[NAME_VALIDATOR])
    efficiency = models.FloatField()
    rating = models.FloatField()
    position = models.CharField(
        choices=Position.choices,
        null=True,
        default=None,
    )

    class Meta:
        unique_together = ['sector_number', 'row_number', 'place_number']


class PlayerStatistic(models.Model):
    """

    """

    count_matches = models.PositiveIntegerField()
    count_goals = models.PositiveIntegerField()
    count_goals_conceded = models.PositiveIntegerField()
    count_goals_pass = models.PositiveIntegerField()
    count_penalties = models.PositiveIntegerField()
    player_id = models.ForeignKey(Player, on_delete=models.SET_NULL, on_update=models.CASCADE)


class TypeTicket(models.Model):
    """
    Модель Тип Билета

    Атрибуты:
        price: цена билета
        type: тип ("VIP", ...)

    """

    class Type(models.TextChoices):
        VIP = "VIP"
        STANDARD = "STANDARD"
        CHILD = "CHILD"

    price = models.PositiveIntegerField()
    type = models.CharField(
        max_length=15,
        choices=Type.choices,
        default=Type.STANDARD,
    )


class CashMachine(models.Model):
    """
    Модель Касса

    Атрибуты:

    """

    total_tickets = models.PositiveIntegerField()
    sold_tickets = models.PositiveIntegerField()
    remaining_tickets = models.PositiveIntegerField()
    money_from_sale = models.PositiveIntegerField()


class Ticket(models.Model):
    """

    """

    sold = models.BooleanField(default=False)
    sector_number = models.PositiveIntegerField()
    row_number = models.PositiveIntegerField()
    place_number = models.PositiveIntegerField()
    cash_machine_id = models.ForeignKey(CashMachine, on_delete=models.SET_NULL, on_update=models.CASCADE)
    type_ticket_id = models.ForeignKey(TypeTicket, on_delete=models.CASCADE, on_update=models.CASCADE)
    match_id = models.ForeignKey(Match, on_delete=models.SET_NULL, on_update=models.CASCADE)
