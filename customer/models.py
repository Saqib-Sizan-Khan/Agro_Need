from django.db import models

# Create your models here.

class Customer(models.Model):
    customerName = models.CharField(max_length=20)
    customerEmail = models.EmailField(max_length=50)
    customerContact = models.CharField(max_length=11)
    customerPassword = models.CharField(max_length=20)