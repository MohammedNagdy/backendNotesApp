from django.db import models

# model for the notes

class NotesModel(models.Model):
	note = models.TextField(blank=False)
