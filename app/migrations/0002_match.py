# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('goalsf', models.IntegerField(default=0)),
                ('golasl', models.IntegerField(default=0)),
                ('hour', models.DateTimeField()),
                ('draw', models.BooleanField(default=False)),
                ('ligue', models.ForeignKey(to='app.Ligue')),
                ('lose', models.ForeignKey(related_name='loser', to='app.Team', null=True)),
                ('teamf', models.ForeignKey(related_name='team2', to='app.Team', null=True)),
                ('teaml', models.ForeignKey(related_name='team1', to='app.Team', null=True)),
                ('win', models.ForeignKey(related_name='winner', to='app.Team', null=True)),
            ],
        ),
    ]
