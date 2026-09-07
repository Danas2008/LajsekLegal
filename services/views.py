from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from core.seo import ld_json

TEMPLATE_BY_SLUG = {
    'spory-a-mediace': 'spory-a-mediace.html',
    'nemovitosti': 'nemovitosti.html',
    'smlouvy': 'smlouvy.html',
    'dusevni-vlastnictvi': 'dusevni-vlastnictvi.html',
    'gdpr': 'gdpr.html',
    'mediace': 'mediace.html',
}

SERVICE_NAMES = {
    'spory-a-mediace': 'Soudní spory a mediace',
    'nemovitosti': 'Nemovitosti',
    'smlouvy': 'Smlouvy',
    'dusevni-vlastnictvi': 'Duševní vlastnictví',
    'gdpr': 'Osobní údaje a GDPR',
    'mediace': 'Mediace',
}


def service_detail(request, slug):
    template_name = TEMPLATE_BY_SLUG.get(slug)
    if template_name is None:
        raise Http404

    site_url = settings.SITE_URL.rstrip('/')
    breadcrumb_schema = ld_json({
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Domů', 'item': site_url + reverse('home')},
            {'@type': 'ListItem', 'position': 2, 'name': SERVICE_NAMES[slug], 'item': site_url + reverse('service_detail', args=[slug])},
        ],
    })

    return render(request, template_name, {'breadcrumb_schema': breadcrumb_schema})
