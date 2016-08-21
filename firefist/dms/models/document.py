from core.models import FirefistDocumentCore
from django.db import models
from administration.models import FirefistUser
from dms.models import Directory


class Document(FirefistDocumentCore):
    owner = models.ForeignKey(FirefistUser)
    location = models.FileField(upload_to='/files')
    directory = models.ForeignKey(Directory)
    class Meta:
        permissions = (
            ('view', 'can view file'),
            ('delete', 'delete file'),
            ('update', 'can update meta data'),
            )