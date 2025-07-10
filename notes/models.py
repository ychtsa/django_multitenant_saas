from django.db import models
from django.utils.text import slugify


class Note(models.Model):
    """
    Note model belonging to a tenant (automatically linked via current schema).
    - slug: unique identifier for friendly URLs
    """
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug based on the title if not provided
        if not self.slug:
            base = slugify(self.title) or "note"
            slug = base
            i = 1
            while Note.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
