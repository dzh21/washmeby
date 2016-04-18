from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CarWash(models.Model):
	# Address
    address = models.CharField(max_length=255)
    # Work time
    # Busy
    # Price
    # Sale
    # GeoPoint
    def __unicode__(self):
        return self.address
    