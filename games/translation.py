from modeltranslation.translator import register, TranslationOptions
from .models import Game


@register(Game)
class GameTranslateOptions(TranslationOptions):
    fields = ["name", "description"]


