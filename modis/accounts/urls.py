from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
]