from django.db import models


class Product(models.Model):
    year = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    price_beef_kilo = models.CharField(max_length=100)
    price_rice_kilo = models.CharField(max_length=100)
    price_coffee_kilo = models.CharField(max_length=100)
    inflation_rate = models.CharField(max_length=100)