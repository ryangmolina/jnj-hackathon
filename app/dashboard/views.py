from django.shortcuts import render

from app.core.views import LoginGenericView


class DashboardView(LoginGenericView):
    template_name = 'dashboard/index.html'
