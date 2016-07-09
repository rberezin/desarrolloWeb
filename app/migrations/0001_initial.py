# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ligue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('goalsf', models.IntegerField(default=0, blank=True)),
                ('golasl', models.IntegerField(default=0, blank=True)),
                ('hour', models.DateTimeField()),
                ('draw', models.BooleanField(default=False)),
                ('ligue', models.ForeignKey(to='app.Ligue')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut', models.CharField(unique=True, max_length=12)),
                ('phone', models.CharField(max_length=20)),
                ('captain', models.BooleanField(default=False)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('ligue', models.ForeignKey(to='app.Ligue')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='app.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='lose',
            field=models.ForeignKey(related_name='loser', to='app.Team', null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='teamf',
            field=models.ForeignKey(related_name='team2', to='app.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='teaml',
            field=models.ForeignKey(related_name='team1', to='app.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='win',
            field=models.ForeignKey(related_name='winner', to='app.Team', null=True),
        ),
    ]
