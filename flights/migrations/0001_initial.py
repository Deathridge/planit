# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('Carrier', models.CharField(max_length=255, null=True, blank=True)),
                ('FlightCode', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('DepartureDate', models.DateField(null=True, blank=True)),
                ('ArrivalDate', models.DateField(null=True, blank=True)),
                ('DepartureTime', models.TimeField(null=True, blank=True)),
                ('ArrivalTime', models.TimeField(null=True, blank=True)),
                ('DepartureLocation', models.CharField(max_length=255, null=True, blank=True)),
                ('ArrivalLocation', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
