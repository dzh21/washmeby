from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import CarWash

admin.site.register(CarWash, LeafletGeoAdmin)
