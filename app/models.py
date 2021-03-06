from django.db import models
from django.contrib.auth.models import User


class Ligue(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  # For Python 2, use __str__ on Python 3
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128)
    ligue = models.ForeignKey(Ligue)

    def __unicode__(self):
        return unicode(self.name)


class Player(models.Model):
    name = models.CharField(max_length=128)
    user = models.OneToOneField(User)
    rut = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team)
    edad = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.name)


class Match(models.Model):
    ligue = models.ForeignKey(Ligue)
    date = models.DateField()
    goalsf = models.IntegerField(default=0, blank=True)
    golasl = models.IntegerField(default=0, blank=True)
    teaml = models.ForeignKey(Team, related_name='team1')
    teamf = models.ForeignKey(Team, related_name='team2')
    hour = models.DateTimeField()
    win = models.ForeignKey(Team, blank=True, null=True, related_name='winner')
    lose = models.ForeignKey(Team, blank=True, null=True, related_name='loser')
    draw = models.BooleanField(default=False)