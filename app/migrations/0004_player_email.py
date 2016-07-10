# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_player_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='email',
            field=models.CharField(default=datetime.datetime(2016, 7, 10, 1, 55, 55, 649182, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
