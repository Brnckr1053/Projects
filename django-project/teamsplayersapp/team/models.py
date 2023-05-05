from django.db import models

# Create your models here.


class Team(models.Model):
    city = models.CharField(max_length=50)
    mascot = models.CharField(max_length=50)

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teams = models.ManyToManyField(Team)
