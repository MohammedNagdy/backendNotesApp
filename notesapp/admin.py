from django.contrib import admin
from .models import NotesModel


# register the admin (note , note123)
admin.site.register(NotesModel)