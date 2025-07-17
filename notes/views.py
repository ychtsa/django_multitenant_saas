from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Note
from .serializers import NoteSerializer

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD API for Note:
    - list(), retrieve(), create(), update(), destroy()
    - lookup_field = 'slug' so URLs use slug instead of pk
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = "slug"
    filter_backends = [OrderingFilter]
    ordering_filter = ['created_at', 'updated_at', 'title']
