from django.shortcuts import render

from app.core.views import LoginGenericView


class ServicesView(LoginGenericView):
    template_name = 'services/index.html'


class JobChangeRequestView(LoginGenericView):
    template_name = 'services/job-change-request.html'


class CertificateOfEmploymentRequestView(LoginGenericView):
    template_name = 'services/certificate-of-employment-request.html'


class TrackingView(LoginGenericView):
    template_name = 'services/tracking.html'
