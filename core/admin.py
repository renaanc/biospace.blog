from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Artigo

# Register your models here.
@admin.register(Artigo)
class ArtigoAdmin(TranslatableAdmin):
    list_display = ['__str__', 'publicado_em']

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 60px;" />', obj.image.url)
        return "-"
    thumbnail_preview.short_description = "Preview"



