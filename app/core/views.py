import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View


class GenericView(View):
    """Base view that every view should inherit from.

    Adds a default `user` instance to the context data

    """
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = {}
        self.user = self.request.user
        context['user'] = self.user
        context['notify'] = json.dumps({})
        context['dump'] = json.dumps({})
        context.update(**kwargs)
        return context

    def get(self, request, *args,  **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class LoginGenericView(LoginRequiredMixin, GenericView):
    """Any core view that requires a login redirect should inherit from.

    """
    login_url = 'account_login'


class MultipleFieldLookupMixin(object):
    """Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field
    filtering.

    See: http://www.django-rest-framework.org/api-guide/generic-views/
         #creating-custom-mixins

    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            filter[field] = self.kwargs[field]
        return get_object_or_404(queryset, **filter)  # Lookup the object
