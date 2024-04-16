from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.forms import ValidationError
# Create your models here.


class CardModel(models.Model):
    image = models.ImageField(upload_to="img/%y")
    title = models.CharField(max_length=100)
    details = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    

class ChefModel(models.Model):
    image = models.ImageField(upload_to="img/%y")
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    

class Comments(models.Model):
    content = models.TextField(max_length=255)
    user = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

