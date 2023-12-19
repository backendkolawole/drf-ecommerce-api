from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    company = models.CharField(max_length=50)
    rating = models.IntegerField(default=4.5)
    featured = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)
    
