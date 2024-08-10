from django.urls import path
from django.views import View

from . import views
from .views import filterTask

urlpatterns = [
    path('', views.home, name='home'),
    path('filter', filterTask.as_view(), name='filter'),
]