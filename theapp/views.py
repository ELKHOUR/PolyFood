from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from theapp.models import CardModel, ChefModel, Comments
from django.views.generic import CreateView, ListView
from theapp.forms import FormAddComments
# Create your views here.

def home(request):
    cards = CardModel.objects.all()[:8]
    chefs = ChefModel.objects.all()
    comments = Comments.objects.all()
    return render(request, 'base.html',
                  { 'cards':cards,
                    'chefs':chefs,
                    'comments':comments
                    })


class menuView(ListView):
    model = CardModel
    template_name = 'menu/allmenu.html'
    context_object_name = 'cards'




class AddComment(CreateView):
    model = Comments
    template_name = "addcomments/add.html"
    form_class = FormAddComments

    success_url = reverse_lazy('home')
