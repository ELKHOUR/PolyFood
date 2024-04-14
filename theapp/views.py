from django.shortcuts import render
from .models import CardModel, ChefModel
# Create your views here.

def home(request):
    cards = CardModel.objects.all()
    chefs = ChefModel.objects.all()
    return render(request, 'base.html',{'cards':cards,'chefs':chefs})