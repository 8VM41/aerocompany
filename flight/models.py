# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from airport.models import Airport


class Flight(models.Model):
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    ECONOMY_CLASS = 'E'
    CLASS_OF_SERVICE = (
        (FIRST_CLASS, 'First'),
        (BUSINESS_CLASS, 'Business'),
        (ECONOMY_CLASS, 'Economic'),
    )
    flight_number = models.CharField(max_length=8, verbose_name='Flight Number')
    departure_airport = models.ForeignKey(Airport, verbose_name='Departure airport', default='',
                                          related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, verbose_name='Arrival airport', default='',
                                        related_name='arrival_airport')
    departure_date_begin = models.DateField(verbose_name='Departure date begin', default=timezone.datetime.now().date())
    arrival_date_begin = models.DateField(verbose_name='Arrival date begin', default=timezone.datetime.now().date())
    repeat_interval = models.IntegerField(verbose_name='Repeat interval', default=1)
    departure_time = models.TimeField(verbose_name='Departure time', default="08:00")
    arrival_time = models.TimeField(verbose_name='Arrival time', default="10:00")

    def __unicode__(self):
        return '{} : {} {} {} -> {} {} {} : repeat = {}'.format(self.flight_number, self.departure_date_begin,
                                                                     self.departure_time, self.departure_airport,
                                                                     self.arrival_airport, self.arrival_date_begin,
                                                                     self.arrival_time, self.repeat_interval)