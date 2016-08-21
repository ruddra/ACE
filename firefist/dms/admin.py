from django.contrib import admin

# Register your models here.

from .models import Document, Directory

admin.site.register(Document, Directory)