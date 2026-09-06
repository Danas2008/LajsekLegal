from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from core.models import TextBlock

register = template.Library()


@register.simple_tag
def edit(key, default=''):
    """Vypíše editovatelný text; pokud admin obsah přepsal, vrátí uloženou verzi z DB."""
    stored = TextBlock.objects.filter(key=key).values_list('content', flat=True).first()
    content = stored if stored is not None else default
    return mark_safe(f'<span class="editable" data-edit-key="{escape(key)}">{content}</span>')
