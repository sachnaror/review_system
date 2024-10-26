# myproject/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin  # Import the admin module
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Now admin will be recognized
    path('', include('reviews.urls')),  # Include your review app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

