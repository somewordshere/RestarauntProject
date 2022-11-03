from django.db import models


class menuItem(models.Model):
    category = models.CharField(max_length=50)
    price = models.FloatField()
    name = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)