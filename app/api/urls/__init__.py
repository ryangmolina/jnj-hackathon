import notifications.urls

from django.conf.urls import url, include

from .accounts import accounts_patterns
from .services import services_patterns
from .personalizations import personalizations_patterns


app_name = 'api'
urlpatterns = [
    url(
        r'^services/',
        include(services_patterns),
        name='services'
    ),
    url(
        r'^accounts/',
        include(accounts_patterns),
        name='accounts',
    ),
    url(
        r'^personalizations/',
        include(personalizations_patterns),
        name='personalizations'
    ),
    url(
        r'^inbox/notifications/',
        include(notifications.urls, namespace='notifications')
    ),
]