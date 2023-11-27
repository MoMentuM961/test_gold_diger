from django.db import models


# Create your models here.

class GoldPrice(models.Model):
    price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
