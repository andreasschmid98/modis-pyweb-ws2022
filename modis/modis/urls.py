from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Get all paths from base.urls
    path('', include('accounts.urls')),  # Get all paths from accounts.urls
]
