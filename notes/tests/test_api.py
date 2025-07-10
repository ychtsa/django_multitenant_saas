import pytest
from django.urls import reverse
from rest_framework import status
from notes.models import Note

pytestmark = pytest.mark.django_db


def test_create_note_via_api(api_client):
    url = reverse("note-list")
    payload = {"title": "REST test", "body": "API content"}

    resp = api_client.post(url, payload, format="json")
    assert resp.status_code == status.HTTP_201_CREATED

    data = resp.json()
    note = Note.objects.get(pk=data["id"])
    assert note.title == payload["title"]
    assert note.body == payload["body"]
