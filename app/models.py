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
        return unicode(self.id)


class Player(models.Model):
    user = models.OneToOneField(User)
    rut = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=20)
    captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team)
    edad = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username
