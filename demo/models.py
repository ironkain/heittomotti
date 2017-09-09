from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone


class Tilaus(models.Model):   
    author = models.ForeignKey('auth.User')

    nimi = models.CharField(max_length=50)
    osoite = models.CharField(max_length=50)
    maara = models.CharField(max_length=50)
    puhelin = models.CharField(max_length=50)
    sposti = models.CharField(max_length=50)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title