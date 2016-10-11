from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)

class Topping(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)


