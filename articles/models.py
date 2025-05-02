from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.utils.text import slugify


class Article(TranslatableModel):
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    published = models.BooleanField(_("Publicado"), default=False)

    translations = TranslatedFields(
        title=models.CharField(_("Título"), max_length=200),
        content=models.TextField(_("Conteúdo"))
    )

    tags = models.ManyToManyField('Tag', verbose_name=_("Tags"), blank=True)
    image = models.ImageField(_("Imagem"), upload_to='articles/', null=True, blank=True)
    source = models.URLField(_("Fonte"), null=True, blank=True)

    FONT_SIZES = [
        ('small', _("Pequeno")),
        ('medium', _("Médio")),
        ('large', _("Grande")),
    ]
    font_size = models.CharField(_("Tamanho da fonte"), max_length=10, choices=FONT_SIZES, default='medium')

    def save(self, *args, **kwargs):
        if not self.slug:
            # Gera o slug com base no título na linguagem ativa ou qualquer disponível
            self.slug = slugify(self.safe_translation_getter('title', any_language=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
