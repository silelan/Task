from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Halanx Admin"
admin.site.site_title = "Halanx Admin Portal"
admin.site.index_title = "Welcome to Halanx Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('accounts.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)