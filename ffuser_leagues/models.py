from django.db import models
from platforms.models import Platform


class League(models.Model):
    platform = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    league_id = models.CharField(max_length=200)
    season_year = models.DateField(default=2022)
    current_status = models.CharField(max_length=150)
    # => "pre-draft", "drafting", "in-season", "completed"
    previous_league_id = models.CharField(max_length=200)
    # league renewed for next year => new league_id
    league_settings = models.CharField(max_length=300)
    #  => scoring settings, number of teams
    scoring_settings = models.CharField(max_length=300)
    league_type = models.CharField(max_length=150)
    #  => Dynasty, Keeper, "Regular"
    transactions = models.CharField(max_length=300)
    trades = models.CharField(max_length=300)
    league_users = models.CharField(max_length=200)
    league_drafts = models.CharField(max_length=200)
    trending_players = models.CharField(max_length=200)


class LeagueUser(models.Model):
    username = models.CharField(max_length=150)
    user_id = models.CharField(max_length=150)
    display_name = models.CharField(max_length=150)
    roster = models.CharField(max_length=350)


class LeagueMatchup(models.Model):
    matchup_id = models.CharField(max_length=200)
    teams = models.CharField(max_length=200)
    week = models.CharField(max_length=200)
    point_totals = models.IntegerField()
    starters = models.CharField(max_length=200)
    players = models.CharField(max_length=300)


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=100)
    # => Trade, Free_agent, waiver wire, drop,
    transaction_id = models.CharField(max_length=200)
    roster_ids = models.CharField(max_length=200)
    # => Teams involved in a specific transaction
    transaction_week = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    consenter_ids = models.CharField(max_length=100)
    player_added = models.CharField(max_length=200)
    player_dropped = models.CharField(max_length=200)


class LeagueDraft(models.Model):
    draft_id = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    # => Only show completed drafts from previous seasons or the countdown clock
    league_id = models.CharField(max_length=100)
