from django.conf.urls import url

from .views import (
    ServicesView,
    JobChangeRequestView,
    TrackingView,
)


app_name = 'services'
urlpatterns = [
    url(
        r'^$',
        ServicesView.as_view(),
        name='index',
    ),
    url(
        r'^job-change-request/$',
        JobChangeRequestView.as_view(),
        name='job_change_request',
    ),
    url(
        r'^tracking/$',
        TrackingView.as_view(),
        name='tracking',
    ),
]
