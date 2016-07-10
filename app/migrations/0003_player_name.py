# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160708_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 7, 10, 1, 15, 17, 440561, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
