from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

import hrms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hrms.urls', namespace = 'hrms')),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
