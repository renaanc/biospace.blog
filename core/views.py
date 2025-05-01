from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language

def home(request):
    print(f"Idioma atual: {get_language()}")  # Só para debug
    title = _("Bem-vindo ao Biospace")  # Tradução (caso precise passar para o template)
    return render(request, 'core/home.html', {'title': title})

def articles(request):
    return render(request, 'articles/article_list.html')

# Página Sobre
def about(request):
    title = _("Sobre o Biospace")  # Tradução para o título
    description = _("O Biospace é um projeto dedicado à astrobiologia, explorando temas como extremófilos e análogos terrestres.")
    return render(request, 'core/about.html', {'title': title, 'description': description})

# Página de Contato
def contact(request):
    title = _("Contato")  # Tradução para o título
    email = _("Entre em contato conosco através do e-mail: contato@biospace.com")
    return render(request, 'core/contact.html', {'title': title, 'email': email})