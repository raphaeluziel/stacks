from django.urls import path
from . import views

urlpatterns = [

  

    path('person/<int:user_id>/', views.person_detail, name='person_detail'),
    path('person/new/', views.person_create, name='person_create'),
    path('person/<int:user_id>/edit/', views.person_edit, name='person_edit'),
    path('person/list/', views.person_list, name='person_list'),
    path('person/<int:user_id>/delete/', views.person_delete, name='person_delete'),



]