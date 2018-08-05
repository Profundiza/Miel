from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        try:
            if not request.user.is_authenticated and 'login' not in request.resolver_match.view_name:
                return HttpResponseRedirect(reverse('account:login'))
        except AttributeError:
            pass

        # Code to be executed for each request/response after
        # the view is called.

        return response
