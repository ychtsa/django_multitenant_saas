from django.utils.text import slugify
from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Note model:
    - Read-only fields: id, slug, created_at
    - validate_body: ensures body length limit
    - create(): regenerates a unique slug on creation
    """
    class Meta:
        model = Note
        fields = ("id", "slug", "title", "body", "created_at")
        read_only_fields = ("id", "slug", "created_at")

    def validate_body(self, value: str) -> str:
        if len(value) > 5000:
            raise serializers.ValidationError("Body too long (max 5000 chars).")
        return value

    def create(self, validated_data):
        # Ensure slug is unique before saving
        title = validated_data.get("title", "")
        base = slugify(title) or "note"
        slug = base
        i = 1
        while Note.objects.filter(slug=slug).exists():
            slug = f"{base}-{i}"
            i += 1
        validated_data["slug"] = slug
        return super().create(validated_data)
