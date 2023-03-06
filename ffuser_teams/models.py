from django.db import models


class UsersTeam(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    roster_id = models.CharField(max_length=150)
    roster = models.CharField(max_length=150)
    avatar_id = models.CharField(max_length=150)
    league_name = models.CharField(max_length=150)
    transactions = models.CharField(max_length=150)
    draft_picks = models.CharField(max_length=150)
    recent_trades = models.CharField(max_length=150)
    players = models.CharField(max_length=150)
    matchups = models.CharField(max_length=150)
    record = models.CharField(max_length=150)
