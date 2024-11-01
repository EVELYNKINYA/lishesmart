# virtual_culinary_coach/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Ensure this is correct
    path('', include('core.urls')),  # Add this line to include the core URLs at the root
]


