from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-published_at',)
