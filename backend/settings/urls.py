from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("scrap.urls")),
    path('', include("details.urls")),
    path('', include("finalize.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
