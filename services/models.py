from django.db import models

# Create your models here.

class Services(models.Model):
    servicesName = models.CharField(max_length=20)
    servicesPrice = models.FloatField()
