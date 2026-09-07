from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    published_at = models.DateField()
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])
