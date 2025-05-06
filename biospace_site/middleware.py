from django.utils import translation
from django.http import HttpResponseRedirect

def set_language_middleware(get_response):
    def middleware(request):
        path = request.path_info
        if path == "/":
            lang = translation.get_language_from_request(request)
            if lang not in ['en', 'pt-br']:
                lang = 'en'
            return HttpResponseRedirect(f"/{lang}/")
        return get_response(request)
    return middleware


