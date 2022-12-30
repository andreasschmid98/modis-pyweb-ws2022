from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Get all paths from base.urls
    path('', include('accounts.urls')),  # Get all paths from accounts.urls
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
