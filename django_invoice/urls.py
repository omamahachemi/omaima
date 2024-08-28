
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invoice_app.urls')),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,Ddocument_root=settings.MEDIA_ROOT)