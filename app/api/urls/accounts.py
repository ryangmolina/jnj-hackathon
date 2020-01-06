from rest_framework.routers import DefaultRouter

from django.conf.urls import include
from django.urls import path

from ..views.accounts import ProfileViewSet, ProfileRetrieveUpdateAPIView


# router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet)

accounts_patterns = [
    # path('', include(router.urls)),
    path(
        'profiles/',
        ProfileRetrieveUpdateAPIView.as_view(),
        name='profiles',
    )
]