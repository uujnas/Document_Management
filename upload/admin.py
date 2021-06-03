from django.contrib import admin
# from django.db import Directory
from . models import Directory,Create_folder, Rename

# Register your models here.
# from django.db.models import Directory

admin.site.register(Directory)
admin.site.register(Create_folder)
admin.site.register(Rename)
