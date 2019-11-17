from django_js_reverse.views import urls_js

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('app.dashboard.urls', namespace='dashboard')),
    url(r'^forms/', include('app.forms.urls', namespace='forms')),
    url(r'^documents/', include('app.documents.urls', namespace='documents')),
    url(r'^services/', include('app.services.urls', namespace='services')),
    url(r'^user/', include('allauth.urls')),
    url(r'^jsreverse/$', urls_js, name='js_reverse'),
]

# Media Url Route
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
