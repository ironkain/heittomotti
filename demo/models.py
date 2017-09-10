from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone

KOIVUKLAPI_CHOICES = (
    ('2','2 heittomottia = 103,40 eur'),
    ('3','3 heittomottia = 155,10 eur'),
    ('4','4 heittomottia = 206,80 eur'),
    ('5','5 heittomottia = 258,50 eur'),
    ('6','6 heittomottia = 310,20 eur'),
    ('7','7 heittomottia = 361,90 eur'),
    ('8','8 heittomottia = 413,60 eur'),
    ('9','9 heittomottia = 465,30 eur'),
    ('10','10 heittomottia = 517,00 eur'),
    ('11','11 heittomottia = 568,70 eur'),
    ('12','12 heittomottia = 620,40 eur'),
    ('13','13 heittomottia = 672,10 eur'),
    ('14','14 heittomottia = 723,80 eur'),
    ('15','15 heittomottia = 775,50 eur'),
    ('16','16 heittomottia = 827,20 eur'),
    ('17','17 heittomottia = 878,90 eur'),
    ('18','18 heittomottia = 930,60 eur'),
)

class Tilaus(models.Model):   
    # author = models.ForeignKey('auth.User')

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