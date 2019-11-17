from django.conf.urls import url

from .views import (
    ServicesView,
)


app_name = 'services'
urlpatterns = [
    url(
        r'^$',
        ServicesView.as_view(),
        name='services',
    )
]
