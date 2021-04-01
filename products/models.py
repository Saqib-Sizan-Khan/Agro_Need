from django.db import models

class Products(models.Model):
    productName = models.CharField(max_length=20)
    productPrice = models.FloatField()
