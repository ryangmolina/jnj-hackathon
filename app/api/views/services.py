from rest_framework import status, viewsets

from app.services.models import JobChangeRequest
from ..serializers.services import JobChangeRequestSerializer


class JobChangeRequestViewSet(viewsets.ModelViewSet):
    model = JobChangeRequest
    serializer_class = JobChangeRequestSerializer
    queryset = JobChangeRequest.objects.all()
