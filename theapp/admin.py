from django.contrib import admin
from .models import ChefModel, CardModel, Comments
# Register your models here.


admin.site.register(CardModel)
admin.site.register(ChefModel)
admin.site.register(Comments)