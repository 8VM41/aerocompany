# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0001_initial'),
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flight_number', models.CharField(max_length=8, verbose_name=b'Flight Number')),
                ('departure_date_begin', models.DateField(default=datetime.date(2014, 11, 22), verbose_name=b'Departure date begin')),
                ('arrival_date_begin', models.DateField(default=datetime.date(2014, 11, 22), verbose_name=b'Arrival date begin')),
                ('repeat_interval', models.IntegerField(default=1, verbose_name=b'Repeat interval')),
                ('departure_time', models.TimeField(default=b'08:00', verbose_name=b'Departure time')),
                ('arrival_time', models.TimeField(default=b'10:00', verbose_name=b'Arrival time')),
                ('aircraft', models.ForeignKey(related_name='aircraft', default=b'', verbose_name=b'Aircraft', to='aircraft.Aircraft')),
                ('arrival_airport', models.ForeignKey(related_name='arrival_airport', default=b'', verbose_name=b'Arrival airport', to='airport.Airport')),
                ('departure_airport', models.ForeignKey(related_name='departure_airport', default=b'', verbose_name=b'Departure airport', to='airport.Airport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
