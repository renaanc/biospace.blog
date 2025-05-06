from django.http import HttpResponseRedirect
from django.utils import translation


def set_language_middleware(get_response):
    def middleware(request):
        print("Middleware set_language_middleware está sendo chamado")
        if request.path == "/" and not request.path.startswith(('/en/', '/pt-br/')):
            lang = translation.get_language_from_request(request)
            return HttpResponseRedirect(f"/{lang}/")
        return get_response(request)
    return middleware
