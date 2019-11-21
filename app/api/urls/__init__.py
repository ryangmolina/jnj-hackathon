from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url, include

from .services import services_patterns


app_name = 'api'
urlpatterns = [
    url(
        r'^services/',
        include(services_patterns),
        name='services'
    )
]