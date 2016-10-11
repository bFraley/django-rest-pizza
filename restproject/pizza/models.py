from django.db import models

class Pizza(model.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)

class Topping(model.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=10)


