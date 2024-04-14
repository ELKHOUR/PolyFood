from django.db import models

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
    
