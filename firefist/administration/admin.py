from django.contrib import admin
from .models import FirefistUser, Role

# Register your models here.

admin.site.register(FirefistUser, Role)