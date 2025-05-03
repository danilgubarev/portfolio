from django.contrib import admin
from django.urls import path, include
from gallery.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('sendmess/', include('gallery.urls', namespace='gallery')),
    path('gallery/', include('gallery.urls', namespace='gallery')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
