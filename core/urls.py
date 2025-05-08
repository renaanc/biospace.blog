from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'  # Esta linha é crucial para o namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)