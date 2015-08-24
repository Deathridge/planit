# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_planner_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='protect',
            field=models.BooleanField(default=False),
        ),
    ]
