from .serializers import NoteSerilizer
from rest_framework import permissions,viewsets
from .models import Note
from .forms import NoteForm




class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerilizer
    permision_classes = [permissions.IsAuthenticated]