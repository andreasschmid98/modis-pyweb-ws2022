from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('module/<str:pk>/', views.module, name='module'),
    path('create-module/', views.create_module, name='create-module'),
    path('update-module/<str:pk>/', views.update_module, name='update-module'),
    path('delete-module/<str:pk>/', views.delete_module, name='delete-module'),
    path('fav/<str:pk>/', views.toggle_favourites, name='toggle-fav'),
    path('favourites/', views.favourites, name='favourites'),
    path('sort/<str:direction>/', views.sort, name='sort'),
    path('filter/', views.filter, name='filter'),
]
