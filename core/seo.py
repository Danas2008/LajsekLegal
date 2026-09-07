import json

from django.utils.safestring import mark_safe


def ld_json(data):
    """Serializuje data pro <script type="application/ld+json"> — chrání proti
    předčasnému ukončení tagu, pokud by text obsahoval "</script>"."""
    return mark_safe(json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
