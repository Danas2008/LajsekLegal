from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from core.models import TextBlock

register = template.Library()


@register.simple_tag
def edit(key, default=''):
    """Vypíše krátký editovatelný text (nadpis, jedna věta); ukládá se přes API na blur."""
    stored = TextBlock.objects.filter(key=key).values_list('content', flat=True).first()
    content = stored if stored is not None else default
    return mark_safe(f'<span class="editable" data-edit-key="{escape(key)}">{content}</span>')


class EditBlockNode(template.Node):
    def __init__(self, key, nodelist):
        self.key = key
        self.nodelist = nodelist

    def render(self, context):
        stored = TextBlock.objects.filter(key=self.key).values_list('content', flat=True).first()
        content = stored if stored is not None else self.nodelist.render(context)
        return f'<div class="editable" data-edit-key="{escape(self.key)}">{content}</div>'


@register.tag('editblock')
def do_editblock(parser, token):
    """Obalí celý blok HTML (odstavce, seznamy, citace) jako jeden editovatelný celek."""
    bits = token.split_contents()
    if len(bits) != 2:
        raise template.TemplateSyntaxError('editblock tag takes exactly one argument: the key')
    key = bits[1].strip('"\'')
    nodelist = parser.parse(('endeditblock',))
    parser.delete_first_token()
    return EditBlockNode(key, nodelist)
