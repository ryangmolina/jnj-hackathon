from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response

from app.personalizations import question_clustering
from ..serializers.accounts import ProfileSerializer


class QuestionClusteringModelAPIView(APIView):
    
    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        birth_date = profile.birth_date
        today = date.today() 
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) 

        form_data = {
            "age": age,
            "compa-ratio": 1,
            "generation": "",
        }
        form_data.update(ProfileSerializer(profile).data)
        return Response(
            question_clustering.predict(form_data),
        )