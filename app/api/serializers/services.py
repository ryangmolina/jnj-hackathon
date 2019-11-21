from rest_framework import serializers

from app.services.models import JobChangeRequest


class JobChangeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobChangeRequest
        fields = '__all__'
