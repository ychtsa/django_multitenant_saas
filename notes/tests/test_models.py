import pytest
from django.utils import timezone
from notes.models import Note
import time

pytestmark = pytest.mark.django_db

class TestNoteModel:
    def test_note_model_create(self):
        note = Note.objects.create(title="model test", body="model content")
        assert note.pk is not None
        assert note.slug
        assert note.created_at is not None
        assert note.updated_at is not None

    def test_note_model_update(self):
        note = Note.objects.create(title="model test", body="model content")
        original_updated_at = note.updated_at
        # Wait a moment to ensure timestamp changes
        time.sleep(1)
        # Update the note
        note.title = "updated title"
        note.save()
        note.refresh_from_db()
        assert note.updated_at > original_updated_at

