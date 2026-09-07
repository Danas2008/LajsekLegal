from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static
from django.utils.html import strip_tags

from core.seo import ld_json

from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    BlogPost.objects.filter(pk=post.pk).update(views=post.views + 1)

    post_schema = ld_json({
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        'headline': post.title,
        'description': (post.excerpt or strip_tags(post.body))[:155],
        'datePublished': post.published_at.isoformat(),
        'image': request.build_absolute_uri(static('img/obrazek1.jpg')),
        'author': {'@type': 'Person', 'name': 'Vladimír Lajsek'},
        'publisher': {
            '@type': 'Organization',
            'name': 'Lajsek Legal',
            'logo': {'@type': 'ImageObject', 'url': request.build_absolute_uri(static('img/ikona.ico'))},
        },
        'mainEntityOfPage': settings.SITE_URL.rstrip('/') + post.get_absolute_url(),
    })

    return render(request, 'blog_detail.html', {'post': post, 'post_schema': post_schema})
