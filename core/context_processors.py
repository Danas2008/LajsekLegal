from django.utils import translation


def language(request):
    lang = translation.get_language()
    return {
        'LANG': lang,
        'DATE_FMT': 'N j, Y' if lang == 'en' else 'd. n. Y',
        'DAY_FMT': 'l, N j, Y' if lang == 'en' else 'l d. n. Y',
    }
