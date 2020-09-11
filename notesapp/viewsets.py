from rest_framework import viewsets
from .models import NotesModel
from .serializers import NotesSerializer 


class NotesViewSet(viewsets.ModelViewSet):
	queryset = NotesModel.objects.all()
	serializer_class = NotesSerializer