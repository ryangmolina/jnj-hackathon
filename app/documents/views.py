from django.shortcuts import render

from app.core.views import LoginGenericView


class DocumentsView(LoginGenericView):
    template_name = 'documents/index.html'
