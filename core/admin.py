from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Artigo
from django.utils.html import format_html



# Register your models here.
@admin.register(Artigo)
class ArtigoAdmin(TranslatableAdmin):
    list_display = ['__str__', 'publicado_em']

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="height: 60px;" />', obj.thumbnail.url)
        return "-"
    thumbnail_preview.short_description = "Thumbnail"





