from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.utils import translation

class SetLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/" and not request.COOKIES.get('django_language'):
            lang = translation.get_language_from_request(request)
            return HttpResponseRedirect(f"/{lang}/")

