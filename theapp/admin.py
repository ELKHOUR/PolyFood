from django.contrib import admin
from .models import CardModel
from .models import ChefModel
# Register your models here.


admin.site.register(CardModel)
admin.site.register(ChefModel)