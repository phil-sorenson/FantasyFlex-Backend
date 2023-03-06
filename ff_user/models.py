from django.db import models
from authentication.models import User


class FlexUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player_shares = models.CharField(max_length=300)
    number_of_leagues = models.CharField(max_length=200)
    # avatar_id = models.CharField(max_length=150)
    team_portfolio = models.CharField(max_length=200)
    imported_leagues = models.CharField(max_length=200)
