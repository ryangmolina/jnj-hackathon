from django.conf.urls import url

from .views import (
    FormsView,
)


app_name = 'forms'
urlpatterns = [
    url(
        r'^$',
        FormsView.as_view(),
        name='index',
    )
]
