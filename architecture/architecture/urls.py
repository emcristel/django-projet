
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('archi/', include('archi.urls')),
    path('', include('archi.urls')),
]
