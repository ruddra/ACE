from core.models import FirefistDocumentCore
from django.db import models
from administration.models import FirefistUser

class Directory(FirefistDocumentCore):
    parent = models.ForeignKey('self', required=False)
    child = models.ForeignKey('self', required=False)
    owner = models.ForeignKey(FirefistUser)

    class Meta:
        permission = (
            ("view", "Can see the folder"),
            ("update", "Can update folder"),
            ("delete", "Can remove folder"),
        )
