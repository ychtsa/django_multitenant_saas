import pytest
from notes.models import Note

pytestmark = pytest.mark.django_db


def test_note_model_create():
    note = Note.objects.create(title="model test", body="model content")
    assert note.pk is not None
    assert note.slug
