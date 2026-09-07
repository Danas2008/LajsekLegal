from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from core.models import TextBlock
from core.translations import EN

register = template.Library()


@register.simple_tag(takes_context=True)
def t(context, key, default=''):
    """Krátký UI text (menu, patička, tlačítka) přeložený do angličtiny podle aktuálního jazyka."""
    if context.get('LANG') == 'en':
        return EN.get(key, default)
    return default


@register.simple_tag(takes_context=True)
def edit(context, key, default=''):
    """Vypíše krátký editovatelný text (nadpis, jedna věta); ukládá se přes API na blur.
    Dokud ho admin nepřepíše, v angličtině se použije překlad z core.translations."""
    stored = TextBlock.objects.filter(key=key).values_list('content', flat=True).first()
    if stored is not None:
        content = stored
    elif context.get('LANG') == 'en':
        content = EN.get(key, default)
    else:
        content = default
    return mark_safe(f'<span class="editable" data-edit-key="{escape(key)}">{content}</span>')


class EditBlockNode(template.Node):
    def __init__(self, key, nodelist):
        self.key = key
        self.nodelist = nodelist

    def render(self, context):
        stored = TextBlock.objects.filter(key=self.key).values_list('content', flat=True).first()
        if stored is not None:
            content = stored
        elif context.get('LANG') == 'en':
            content = EN.get(self.key, self.nodelist.render(context))
        else:
            content = self.nodelist.render(context)
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
