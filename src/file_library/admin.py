from django.contrib import admin
from .models import File, FileUploader
# Register your models here.

admin.site.register(FileUploader)
admin.site.register(File)
