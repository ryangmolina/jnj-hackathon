from django.shortcuts import render

from app.core.views import LoginGenericView


class ServicesView(LoginGenericView):
    template_name = 'services/index.html'


class JobChangeRequestView(LoginGenericView):
    template_name = 'services/job-change-request.html'