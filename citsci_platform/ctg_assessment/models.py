from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
import uuid
from ..models import TimeStampedModel
from ..projects.models import Project, ProjectTask

# Create your models here.

class Assessment(TimeStampedModel):
    name = models.CharField(max_length=100)

    # FK to project (in separate database, hence not models.ForeignKey)
    project_id = models.UUIDField(default=uuid.uuid4)

    # FK to user (in separate database, hence not models.ForeignKey)
    user_id = models.UUIDField(default=uuid.uuid4)
