from core.models import FirefistCore
from django.contrib.auth.models import User
from enum import Enum


class FirefistUser(FirefistCore):
    user_types = [
        ('admin', 1),
        ('standard', 2),
        ('superadmin', 3)
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=self.user_types, default=2)
