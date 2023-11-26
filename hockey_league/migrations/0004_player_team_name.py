# Generated by Django 4.2.7 on 2023-11-26 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hockey_league', '0003_alter_player_first_name_alter_player_second_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hockey_league.team'),
        ),
    ]
