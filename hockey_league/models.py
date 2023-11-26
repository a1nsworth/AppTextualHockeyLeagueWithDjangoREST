from django.db import models
from django.core.validators import RegexValidator


class HockeyLeague(models.Model):
    """
    Модель Хоккейная Лига

    Атрибуты:
        name: название лиги
    """

    name = models.CharField(max_length=100, primary_key=True)


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
    hockey_league_name = models.ForeignKey(HockeyLeague, null=True, on_delete=models.SET_NULL)


class Team(models.Model):
    """
    Модель Команда

    Атрибуты:
        name: название комманды
        popularity: популярность команды
        season_id: айди сезона
    """

    name = models.CharField(max_length=30, primary_key=True)
    popularity = models.FloatField()
    season_id = models.ForeignKey(Season, unique=False, null=True, on_delete=models.SET_NULL)


class Match(models.Model):
    """
    Модель Матч

    Атрибуты:
        location: место проведения
        date_time_start: дата и время начала матча
        spend_money: потраченные деньги на организацию матча
        opponent_team_id_1: айди команды противника
        opponent_team_id_2: айди команды противника
    """

    location = models.CharField(max_length=50)
    date_time_start = models.DateTimeField()
    spend_money = models.FloatField()
    opponent_1_name = models.ForeignKey(Team, related_name='opponent_1_id', null=True,
                                        on_delete=models.SET_NULL, )
    opponent_2_name = models.ForeignKey(Team, related_name='opponent_2_id', null=True,
                                        on_delete=models.SET_NULL,
                                        )


class Player(models.Model):
    """
    Модель Игрок

    Атрибуты:
        first_name: имя
        second_name: фамилия
        efficiency: эффективность
        rating: рейтинг
        position: позиция
    """

    class Position(models.TextChoices):
        FORWARD = "FORWARD"
        DEFENSE = "DEFENSE"
        GOALIE = "GOALIE"

    NAME_VALIDATOR = RegexValidator(
        regex='^[A-Z][a-z]{1,}$',
        message='Имя должно содержать только буквы английского алфавита алфавита и начинаться с Заглавной буквы.',
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
        max_length=30,
    )
    team_name = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)


class PlayerStatistic(models.Model):
    """
    Модель Статистика Игрока

    Атрибуты:
        count_matches: кол-во матчей
        count_goals: кол-во голов
        count_goals_conceded: голов пропущено
        count_goals_pass: количество гол + пас
        count_penalties: количество штрафных
        player_id: айди игрока
    """

    count_matches = models.PositiveIntegerField()
    count_goals = models.PositiveIntegerField()
    count_goals_conceded = models.PositiveIntegerField()
    count_goals_pass = models.PositiveIntegerField()
    count_penalties = models.PositiveIntegerField()
    player_id = models.OneToOneField(Player, null=True, on_delete=models.SET_NULL)


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
        total_tickets: всего билетов
        sold_tickets: проданных билетов
        remaining_tickets: оставшихся билетов
        money_from_sale: денег с продажи
    """

    total_tickets = models.PositiveIntegerField()
    sold_tickets = models.PositiveIntegerField()
    remaining_tickets = models.PositiveIntegerField()
    money_from_sale = models.PositiveIntegerField()


class Ticket(models.Model):
    """
    Модель Билет

    Атрибуты:
        sold: продан билет или нет
        sector_number: номер сектора
        row_number: номер ряда
        place_number: номер места
        cash_machine_id: айди кассы
        type_ticket_id: айди типа билета
        match_id: айди матча
    """

    sold = models.BooleanField(default=False)
    sector_number = models.PositiveIntegerField()
    row_number = models.PositiveIntegerField()
    place_number = models.PositiveIntegerField()
    cash_machine_id = models.ForeignKey(CashMachine, null=True, on_delete=models.SET_NULL)
    type_ticket_id = models.ForeignKey(TypeTicket, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ['sector_number', 'row_number', 'place_number']
