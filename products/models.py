from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField()
    quantity = models.CharField()
    size = models.CharField()
    price = models.CharField()
    
    def __str__(self):
        return self.name
    

class AccessToken(models.Model):
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        get_latest_by = 'created_at'
    
    def __str__(self):
        return self.token