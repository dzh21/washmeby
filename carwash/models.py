from __future__ import unicode_literals

from djgeojson.fields import PointField
from django.db import models
from django.contrib.auth.models import User


class CarWash(models.Model):
	# Address
    address = models.CharField(max_length=255)
    # Work time
    # Busy
    # Price
    # Sale
    geom = PointField()
    fk_owner = models.ForeignKey(User)

    @property
    def popupContent(self):
        return '{}'.format(
            self.address
        )

    def __unicode__(self):
        return self.address
    