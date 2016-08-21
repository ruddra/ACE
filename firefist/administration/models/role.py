from core.models import FirefistCore
from django.db import models


class Role(FirefistCore):
    name = models.CharField(max_length=255)