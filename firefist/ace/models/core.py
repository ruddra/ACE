from django.db import models
from ace.mixins import FirefistMixin


class FCore(models.model, FirefistMixin):
    date_created = models.BigIntegerField()
    last_updated = models.BigIntegerField()


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

