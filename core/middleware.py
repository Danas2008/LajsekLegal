from django.utils import translation


class SessionLanguageMiddleware:
    """Aktivuje jazyk uložený v session (přepínač CS/EN v menu) pro Django i18n
    (formátování dat apod.), viz core.views.set_language."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.session.get('site_lang', 'cs')
        translation.activate(lang)
        request.LANGUAGE_CODE = translation.get_language()
        response = self.get_response(request)
        translation.deactivate()
        return response
