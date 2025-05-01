from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),  # Aqui será acessado como /pt-br/articles/ ou /en/articles/
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]
