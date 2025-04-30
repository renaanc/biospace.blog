from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Article, Tag

@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    list_display = ('title', 'created_at', 'font_size', 'slug')
    list_filter = ('tags', 'font_size')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
