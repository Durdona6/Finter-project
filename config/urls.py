from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.url') ),
    path('about/', include('about.urls') ),
    path('services/', include('services.url') ),
    path('team/', include('team.url') ),
    path('contact/', include('contact_us.url') ),
    path('login/',include('login.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)