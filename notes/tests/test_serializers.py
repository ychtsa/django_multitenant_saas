import pytest
from notes.serializers import NoteSerializer

pytestmark = pytest.mark.django_db


class TestNoteSerializer:
    def test_serializer_valid(self):
        ser = NoteSerializer(data={"title": "Hello", "body": "World"})
        assert ser.is_valid()
        note = ser.save()
        assert note.pk is not None

    @pytest.mark.parametrize(
        "payload,field",
        [({"title": ""}, "title"), ({"body": ""}, "body")],
    )
    def test_missing_field(self, payload, field):
        ser = NoteSerializer(data=payload)
        assert not ser.is_valid()
        assert field in ser.errors

    def test_body_too_long(self):
        ser = NoteSerializer(data={"title": "T", "body": "x" * 5001})
        assert not ser.is_valid()
        assert "body" in ser.errors
