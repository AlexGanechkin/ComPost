from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from compost import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('post/', include('posts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
