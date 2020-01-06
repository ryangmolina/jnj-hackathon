from rest_framework.routers import DefaultRouter

from django.conf.urls import include
from django.urls import path

from ..views.services import JobChangeRequestViewSet


router = DefaultRouter()
router.register(r'job-change-requests', JobChangeRequestViewSet)

services_patterns = [
    path('', include(router.urls)),
]