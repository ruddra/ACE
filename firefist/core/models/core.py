from django.db import models
from ace.mixins import FirefistMixin
from datetime import datetime


class FirefistCore(models.model, FirefistMixin):
    date_created = models.BigIntegerField()
    last_updated = models.BigIntegerField()

    class Meta:
        abstruct = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.get_date_created()
        self.get_last_updated()
        super().save(*args, **kwargs)

    def get_date_created(self):
        self.date_created = self.clock()

    def get_last_updated(self):
        self.last_updated = self.clock()


class FirefistDocumentCore(FirefistCore):
    version = models.CharField(required=True)
    meta_data = models.CharField(required=False, null=True, max_length=255)
    comment = models.CharField(required=False, null=True, max_length=255)

    class Meta:
        abstruct = True
