from django.shortcuts import redirect

from app.core.views import LoginGenericView, GenericView


class AccountView(LoginGenericView):
    template_name = 'accounts/index.html'
