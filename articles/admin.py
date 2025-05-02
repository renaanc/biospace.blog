from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Article, Tag

@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    list_display = ('__str__', 'slug', 'published', 'created_at', 'font_size')
    list_filter = ('published', 'tags', 'font_size')
    search_fields = ('translations__title', 'translations__content')
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
