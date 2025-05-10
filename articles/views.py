from django.shortcuts import render, get_object_or_404  # Adicionei a importação do get_object_or_404
from .models import Article
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render


@csrf_protect
def minha_view_com_post(request):
    # Lógica de manipulação de dados POST aqui
    return render(request, 'articles/article_detail.html')

def article_list(request):
    # Filtrando apenas os artigos publicados
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # Usando o slug para buscar o artigo
    article = get_object_or_404(Article, slug=slug, published=True)
    return render(request, 'articles/article_detail.html', {'article': article})
