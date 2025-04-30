from django.urls import path
from . import views

app_name = 'core'  # Esta linha é crucial para o namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('articles/', views.articles, name='articles'),
    path('contact/', views.contact, name='contact'),
]