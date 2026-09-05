from django.http import Http404
from django.shortcuts import render

TEMPLATE_BY_SLUG = {
    'spory-a-mediace': 'spory-a-mediace.html',
    'nemovitosti': 'nemovitosti.html',
    'smlouvy': 'smlouvy.html',
    'dusevni-vlastnictvi': 'dusevni-vlastnictvi.html',
    'gdpr': 'gdpr.html',
    'mediace': 'mediace.html',
}


def service_detail(request, slug):
    template_name = TEMPLATE_BY_SLUG.get(slug)
    if template_name is None:
        raise Http404
    return render(request, template_name)
