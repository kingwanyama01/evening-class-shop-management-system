from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField()
    quantity = models.CharField()
    size = models.CharField()
    price = models.CharField()
    
    def __str__(self):
        return self.name
    
