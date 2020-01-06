from django.urls import path

from ..views.personalizations import QuestionClusteringModelAPIView


personalizations_patterns = [
    path(
        'questions',
        QuestionClusteringModelAPIView.as_view(),
        name='personalized_questions',
    ),
]