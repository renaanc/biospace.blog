from django.http import HttpResponseRedirect
from django.utils import translation

def set_language_middleware(get_response):
    def middleware(request):
        if request.path == "/":
            lang = translation.get_language_from_request(request)
            return HttpResponseRedirect(f"/{lang}/")
        return get_response(request)
    return middleware
