from django.conf.urls import url

from .views import (
    ServicesView,
    JobChangeRequestView,
)


app_name = 'services'
urlpatterns = [
    url(
        r'^$',
        ServicesView.as_view(),
        name='services',
    ),
    url(
        r'^job-change-request/$',
        JobChangeRequestView.as_view(),
        name='job-change-request',
    ),
]
