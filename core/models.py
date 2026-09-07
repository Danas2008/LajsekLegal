from django.db import models


class ContactMessage(models.Model):
    STATUS_NEW = 'new'
    STATUS_RESOLVED = 'resolved'
    STATUS_ARCHIVED = 'archived'
    STATUS_CHOICES = [
        (STATUS_NEW, 'Nevyřešeno'),
        (STATUS_RESOLVED, 'Vyřešeno'),
        (STATUS_ARCHIVED, 'Archiv'),
    ]

    name = models.CharField('Jméno', max_length=120)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefon', max_length=40, blank=True)
    subject = models.CharField('Předmět', max_length=200, blank=True)
    message = models.TextField('Zpráva')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} <{self.email}>'


class TextBlock(models.Model):
    """Editovatelný kus textu na veřejném webu, přepsatelný přímo na stránce (viz core/templatetags/edit_tags.py)."""

    key = models.SlugField(unique=True, max_length=150)
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key
