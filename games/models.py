import os
import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.text import slugify


def game_wasm_directory_path(instance: 'GameVersion', filename: str):
    game_name = instance.game.name
    safe_game_name = slugify(game_name)
    return f"games/{safe_game_name}/wasm/{filename}"


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("name"), max_length=255)
    description = models.TextField(verbose_name=_("description"), null=True, blank=True)
    latest = models.ForeignKey('GameVersion', on_delete=models.SET_NULL, blank=True, null=True, related_name="latest")

    def clean(self):
        super().clean()

        if self.latest:
            if self.latest.game_id != self.id:
                raise ValidationError({
                    'latest': _("The selected version belongs to another game.")
                })
            
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class GameVersion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name=_("game"), related_name="versions")
    version = models.CharField(max_length=20, verbose_name=_("version"))
    wasm_file = models.FileField(
        upload_to=game_wasm_directory_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["wasm"],
                message=_("Only WASM files are allowed.")
            )
        ],
        null=True,
        blank=True,
        verbose_name=_("WASM file")
    )

    def __str__(self):
        return f"{self.game.name} - {self.version}"


def asset_file_path(instance: 'GameVersion', filename: str):
    game_name = instance.version.game.name
    safe_game_name = slugify(game_name)

    folder = instance.target_folder.strip().strip("/")

    if folder:
        return f"games/{safe_game_name}/wasm/{folder}/{filename}"
    else:
        return f"games/{safe_game_name}/wasm/{filename}"
    

class AssetFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.ForeignKey(
        GameVersion, 
        on_delete=models.CASCADE, 
        related_name="assets", 
        verbose_name=_("Game Version")
    )
    target_folder = models.CharField(
        max_length=1024,
        blank=True,
        default="",
        verbose_name=_("Target Folder"),
        help_text=_("e.g. 'resources/music'. Leave empty for root.")
    )

    file = models.FileField(
        upload_to=asset_file_path,
        verbose_name=_("Asset File")
    )

    class Meta:
        verbose_name = _("Asset File")
        verbose_name_plural = _("Asset Files")

    def __str__(self):
        return f"{self.target_folder}/{os.path.basename(self.file.name)}"
