from django.urls import path
from django.views import View

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choose_type/', views.choose_type, name='blog-choose_type'),
    path('poster', views.PostCreate, name='post-create'),
]