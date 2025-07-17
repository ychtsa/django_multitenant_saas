import pytest
from django.urls import reverse
from rest_framework import status
from notes.models import Note
import time

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
    assert data["created_at"] is not None
    assert data["updated_at"] is not None

def test_ordering_by_updated_at(api_client):
    # Create two notes with a time gap
    note1 = Note.objects.create(title="Note 1", body="Content 1")
    time.sleep(1)  # Ensure different timestamps
    note2 = Note.objects.create(title="Note 2", body="Content 2")
    
    url = reverse("note-list") + "?ordering=-updated_at"
    resp = api_client.get(url, format="json")
    assert resp.status_code == status.HTTP_200_OK
    data = resp.json()
    assert len(data['results']) == 2
    assert data['results'][0]["title"] == "Note 2"  # Newer note comes first
    assert data['results'][1]["title"] == "Note 1"