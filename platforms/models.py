from django.db import models


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    user_password = models.CharField(max_length=150)
