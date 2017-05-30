from django.db import models
from django.contrib.postgres.fields import JSONField


class PlaceInformation(models.Model):
    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    longitude = models.FloatField()
    latitude = models.FloatField()
    image = models.CharField()
    comments = JSONField(null=True)

    def __str__(self):
        return self.name
