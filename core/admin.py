from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Artigo



# Register your models here.
@admin.register(Artigo)
class ArtigoAdmin(TranslatableAdmin):
    list_display = ['__str__', 'publicado_em']





