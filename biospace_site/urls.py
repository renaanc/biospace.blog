from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from core.views import language_test_view

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Rota de troca de idioma
]

# i18n_patterns vai adicionar automaticamente o idioma (pt-br, en, etc.)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Aqui está a aplicação principal
    path('articles/', include('articles.urls', namespace='articles')),  # Isso vai incluir as URLs da app articles
)

urlpatterns = [
    path("csrf-test/", language_test_view, name="csrf_test"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


