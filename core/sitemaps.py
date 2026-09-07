from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import BlogPost
from services.views import TEMPLATE_BY_SLUG


class StaticViewSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'

    def items(self):
        return [
            ('home', 1.0),
            ('about', 0.7),
            ('cooperation', 0.6),
            ('fees', 0.6),
            ('references', 0.7),
            ('contact', 0.8),
            ('privacy', 0.2),
            ('blog_list', 0.7),
            ('booking', 0.8),
            ('faq', 0.6),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]


class ServiceSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return list(TEMPLATE_BY_SLUG.keys())

    def location(self, slug):
        return reverse('service_detail', args=[slug])


class BlogSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.published_at

    def location(self, obj):
        return reverse('blog_detail', args=[obj.slug])
