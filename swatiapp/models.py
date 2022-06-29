

from django.db import models


# Create your models here.

class Dynamic(models.Model):
    number = models.IntegerField()
    Context = models.CharField(max_length=20, default='')
    Details = models.CharField(max_length=200, default='')
