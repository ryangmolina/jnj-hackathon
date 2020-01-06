from rest_framework import status, viewsets
from rest_framework.generics import RetrieveUpdateAPIView

from app.accounts.models import Profile
from ..serializers.accounts import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    model = Profile
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    model = Profile
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        return self.request.user.profile

