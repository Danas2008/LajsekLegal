from django.db import models


class Booking(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Čeká na potvrzení'),
        (STATUS_CONFIRMED, 'Potvrzeno'),
        (STATUS_CANCELLED, 'Zrušeno'),
    ]

    datetime = models.DateTimeField()
    client_name = models.CharField('Jméno', max_length=120)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefon', max_length=40, blank=True)
    description = models.TextField('Popis', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return f'{self.client_name} – {self.datetime:%d.%m.%Y %H:%M}'


class Review(models.Model):
    author = models.CharField('Jméno', max_length=120)
    email = models.EmailField('E-mail', blank=True)
    rating = models.PositiveSmallIntegerField('Hodnocení')
    text = models.TextField('Text recenze')
    approved = models.BooleanField('Schváleno', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author} ({self.rating}/5)'


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return self.email


class FAQ(models.Model):
    question = models.CharField('Otázka', max_length=255)
    answer = models.TextField('Odpověď')
    order = models.PositiveIntegerField('Pořadí', default=0)
    active = models.BooleanField('Aktivní', default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return self.question
