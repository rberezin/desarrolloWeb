# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='lose',
            field=models.ForeignKey(related_name='loser', blank=True, to='app.Team', null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='win',
            field=models.ForeignKey(related_name='winner', blank=True, to='app.Team', null=True),
        ),
    ]
