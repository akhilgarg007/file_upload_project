import uuid

from django.core.validators import FileExtensionValidator
from django.db import models

from file_app.storage import grid_fs_storage


class File(models.Model):
    """
    Model to store file metadata and actual file.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=255, unique=True)
    file_summary = models.TextField(blank=True)
    file = models.FileField(validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'pptx'])
        ], storage=grid_fs_storage
    )
