from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from blog import urls
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
