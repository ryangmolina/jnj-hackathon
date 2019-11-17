from django.shortcuts import render

from app.core.views import LoginGenericView


class FormsView(LoginGenericView):
    template_name = 'forms/index.html'
