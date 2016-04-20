from __future__ import unicode_literals

from djgeojson.fields import PointField
from django.db import models

# Create your models here.
class CarWash(models.Model):
	# Address
    address = models.CharField(max_length=255)
    # Work time
    # Busy
    # Price
    # Sale
    geom = PointField()

    @property
    def popupContent(self):
        return '{}'.format(
            self.address
        )

    def __unicode__(self):
        return self.address
    