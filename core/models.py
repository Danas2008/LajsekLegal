from django.db import models


class TextBlock(models.Model):
    """Editovatelný kus textu na veřejném webu, přepsatelný přímo na stránce (viz core/templatetags/edit_tags.py)."""

    key = models.SlugField(unique=True, max_length=150)
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
