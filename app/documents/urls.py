from django.conf.urls import url

from .views import (
    DocumentsView,
)


app_name = 'documents'
urlpatterns = [
    url(
        r'^$',
        DocumentsView.as_view(),
        name='index',
    )
]
