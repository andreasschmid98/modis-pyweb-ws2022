from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')), # go to base.urls
    path('', include('accounts.urls')), # go to accounts.urls
]
