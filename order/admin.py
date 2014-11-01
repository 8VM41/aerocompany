from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from country.models import Country
from flight.models import Flight
from city.models import City
from aircraft.models import Aircraft
from airport.models import Airport


class AircraftAdmin(ModelAdmin):
    model = Aircraft
    list_display = ('company', 'model', 'seat_count')

admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Airport)
admin.site.register(Country)
admin.site.register(City)