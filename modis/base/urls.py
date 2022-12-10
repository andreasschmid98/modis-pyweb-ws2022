from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('module/<str:primary_key>/', views.module, name='module'),
    path('create-module/', views.create_module, name='create-module'),
    path('update-module/<str:primary_key>/', views.update_module, name='update-module'),
    path('delete-module/<str:primary_key>/', views.delete_module, name='delete-module'),
    path('add-fav/<str:module_id>/', views.add_to_favourites, name='add-fav'),
]