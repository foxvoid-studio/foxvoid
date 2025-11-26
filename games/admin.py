from django.contrib import admin
from .models import Game, GameVersion, AssetFile
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin, TabularInline


class AssetFileInline(TabularInline):
    model = AssetFile
    extra = 1
    tab = True
    fields = ["file", "target_folder"]


@admin.register(Game)
class GameAdmin(ModelAdmin, TranslationAdmin):
    list_display = ["name", "creator", "description"]


@admin.register(GameVersion)
class GameVersionAdmin(ModelAdmin):
    list_display = ["game", "version"]
    inlines = [AssetFileInline]


@admin.register(AssetFile)
class AssetFileAdmin(ModelAdmin):
    list_display = ["version__game", "version", "target_folder"]
