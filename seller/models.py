from django.db import models

# Create your models here.

class Seller(models.Model):
    sellerName = models.CharField(max_length=20)
    sellerEmail = models.EmailField(max_length=50)
    sellerContact = models.CharField(max_length=11)
    sellerPassword = models.CharField(max_length=20)
    rating = models.IntegerField()