from rest_framework import serializers
from .models import League

class LeagueSerializer (serializers.ModelSerializer):
  class Meta:
    model= League
    fields= ['id','platform', 'league_id', 'league_name','team', 'type', 'season_year', 'league_details', 'season_year' ]