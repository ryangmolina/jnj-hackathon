from django.conf.urls import url
from .views import AccountView

app_name = 'accounts'
urlpatterns = [
    url(
        r'',
        AccountView.as_view(),
        name='index',
    ),
]
