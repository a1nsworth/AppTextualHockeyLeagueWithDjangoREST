# Generated by Django 4.2.7 on 2023-11-26 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hockey_league', '0002_rename_opponent_1_id_match_opponent_1_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Имя должно содержать только буквы английского алфавита алфавита и начинаться с Заглавной буквы.', regex='^[A-Z][a-z]{1,}$')]),
        ),
        migrations.AlterField(
            model_name='player',
            name='second_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Имя должно содержать только буквы английского алфавита алфавита и начинаться с Заглавной буквы.', regex='^[A-Z][a-z]{1,}$')]),
        ),
    ]
