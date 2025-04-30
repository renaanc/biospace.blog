from django.db import models
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class Artigo(TranslatableModel):
    translations = TranslatedFields(
        titulo=models.CharField(max_length=200),
        conteudo=models.TextField()
    )

    publicado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter('titulo', any_language=True)
