from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone

KOIVUKLAPI_CHOICES = (
    ('2','2 heittomottia = 114,50 eur'),
    ('3','3 heittomottia = 171,75 eur'),
    ('4','4 heittomottia = 229,00 eur'),
    ('5','5 heittomottia = 286,25 eur'),
    ('6','6 heittomottia = 343,50 eur'),
    ('7','7 heittomottia = 400,75 eur'),
    ('8','8 heittomottia = 458,00 eur'),
    ('9','9 heittomottia = 515,25 eur'),
    ('10','10 heittomottia = 572,50 eur'),
)

class Tilaus(models.Model):   
    # author = models.ForeignKey('auth.User')

    title = models.CharField(max_length=50)
    nimi = models.CharField(max_length=50)
    osoite = models.CharField(max_length=50)
    koivuklapeja = models.CharField(max_length=6, choices=KOIVUKLAPI_CHOICES, default='3')
    # maara = models.CharField(max_length=50)
    # color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
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
