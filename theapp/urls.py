from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menuView.as_view(), name='menu'),
    path('addcomment/', views.AddComment.as_view(), name='addcomment')
    
    ]
